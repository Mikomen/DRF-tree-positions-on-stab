from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, status
from rest_framework.response import Response

from .serializer import *

class PositionViewSet(viewsets.ModelViewSet):
    queryset = Position.objects.all()
    serializer_class = PositionSerializer

class LevelViewSet(viewsets.ModelViewSet):
    queryset = Level.objects.all()
    serializer_class = LevelSerializer

class FullEmployerViewSet(viewsets.ModelViewSet):
    queryset = Employers.objects.all()
    serializer_class = FullEmployersSerializer

class EmployerViewSet(viewsets.ModelViewSet):
    queryset = Employers.objects.all()
    serializer_class = EmployersSerializer

