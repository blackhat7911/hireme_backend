from django.shortcuts import render
from user.models import *
from user.serializers import *
from rest_framework import permissions
from rest_framework import generics
from django.contrib.auth.models import User
from knox.models import AuthToken
from rest_framework.response import Response
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from django.contrib.auth import login
from django_filters.rest_framework import DjangoFilterBackend

class ProfileView(generics.ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = (permissions.AllowAny,)
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['accountType','work']

class ProfileDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = (permissions.AllowAny,)

class LocationView(generics.ListCreateAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    permission_classes = (permissions.AllowAny,)
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['city','zipCode']

class LocationDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    permission_classes = (permissions.AllowAny,)

class CoordinatesView(generics.ListCreateAPIView):
    queryset = Coordinates.objects.all()
    serializer_class = CoordinatesSerializer
    permission_classes = (permissions.AllowAny,)

class CoordinatesDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Coordinates.objects.all()
    serializer_class = CoordinatesSerializer
    permission_classes = (permissions.AllowAny,)

class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer
    permission_classes = (permissions.AllowAny,)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1]
        })

class LoginAPI(KnoxLoginView):
    serializer_class = LoginSerializer
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        profile = Profile.objects.get(user=user)
        location = Location.objects.get(user=user)
        return Response({
            "result": "success",
            "datas": {
                "user": UserSerializer(user).data,
                "profile": {
                    "id": profile.id, 
                    "fullname": profile.fullname, 
                    "accountType": profile.accountType,
                    "imageUrl": profile.profile.url,
                    "location": {
                        "name": location.city,
                        "zipCode": location.zipCode,
                        "coordinates": {
                            "id": location.coordinates.id,
                            "lat": location.coordinates.lat,
                            "lng": location.coordinates.lang
                        }
                    },
                "dob": profile.date_of_birth,
                "work": profile.work,
                "joined_at": profile.created_at,
                }
            },
            "token": AuthToken.objects.create(user)[1]   
        })
