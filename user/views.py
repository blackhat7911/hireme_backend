from django.shortcuts import render
from user.models import Profile
from user.serializers import ProfileSerializer, UserSerializer
from rest_framework import permissions
from rest_framework import generics
from django.contrib.auth.models import User

class ProfileView(generics.ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = (permissions.AllowAny,)

class UserView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.AllowAny,)

