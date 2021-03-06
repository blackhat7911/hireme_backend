from django.shortcuts import render
from rest_framework import generics
from work.serializers import *
from work.models import *
from rest_framework import permissions
from user.serializers import UserSerializer
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser

class WorkListView(generics.ListCreateAPIView):
    """
    View for listing all work
    """
    queryset = Work.objects.all()
    serializer_class = WorkSerializer
    permission_classes = (permissions.AllowAny,)
    filter_backends = [DjangoFilterBackend]
    filter_fields = []

class WorkDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    View for displaying a single work
    """
    queryset = Work.objects.all()
    serializer_class = WorkSerializer
    permission_classes = (permissions.AllowAny,)

class RequestList(generics.ListCreateAPIView):
    """
    View for listing all requests
    """
    permission_classes = (permissions.AllowAny,)
    queryset = Request.objects.all()
    serializer_class = RequestSerializer
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['seeker_id', 'worker_id']

class RequestDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    View for displaying a single work
    """
    queryset = Request.objects.all()
    serializer_class = RequestSerializer
    permission_classes = (permissions.AllowAny,)


