from django.shortcuts import render
from user.models import Profile
from user.serializers import ProfileSerializer, UserSerializer, RegisterSerializer
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

class ProfileView(generics.ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = (permissions.AllowAny,)

class ProfileDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
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
    serializer_class = UserSerializer
    serializer_class2 = ProfileSerializer
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        # return Response({
        #     "user_id": user.pk, 
        #     "user": UserSerializer(user, context=self.get_user_serializer_class()).data, 
        #     "profile": ProfileSerializer().data,
        # })
        return super(LoginAPI, self).post(request, format=None)

# class CustomAuthToken(ObtainAuthToken):
#     def post(self, request, *args, **kwargs):
#         serializer = self.serializer_class(data=request.data,
#                                            context={'request': request})
#         serializer.is_valid(raise_exception=True)
#         user = serializer.validated_data['user']
#         token, created = AuthToken.objects.get_or_create(user=user)
#         return Response({
#             'userId': user.pk,
#             'token': token.key,
#             'username': user.username,
#             'email': user.email,
#             # 'phoneNumber': user.profile.phoneNumber,
#             # 'userType': user.profile.user_type,
#             # 'image': user.profile.image.url,
#             # 'joined': user.created_at
#         })
