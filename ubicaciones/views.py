# -*- encoding: utf-8 -*-
#from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly
from rest_framework.decorators import api_view, permission_classes

from models import Via, Pais, Autonomia, Provincia, Municipio
from serializers import ViaSerializer, PaisSerializer, AutonomiaSerializer, ProvinciaSerializer, MunicipioSerializer
  
# http://www.django-rest-framework.org/api-guide/viewsets

@permission_classes((IsAuthenticated, IsAdminUser))
class ViaViewSet(viewsets.ModelViewSet):
	queryset = Via.objects.all()
	serializer_class = ViaSerializer

@permission_classes((IsAuthenticatedOrReadOnly, ))
class PaisViewSet(viewsets.ModelViewSet):
	queryset = Pais.objects.all()
	serializer_class = PaisSerializer

class AutonomiaViewSet(viewsets.ModelViewSet):
	queryset = Autonomia.objects.all()
	serializer_class = AutonomiaSerializer	

class ProvinciaViewSet(viewsets.ModelViewSet):
	queryset = Provincia.objects.all()
	serializer_class = ProvinciaSerializer

class MunicipioViewSet(viewsets.ModelViewSet):
	queryset = Municipio.objects.all()
	serializer_class = MunicipioSerializer

