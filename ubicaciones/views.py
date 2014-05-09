# -*- encoding: utf-8 -*-
#from django.shortcuts import render

from rest_framework import generics, permissions, viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from models import Via, Pais, Autonomia, Provincia, Municipio
from serializers import ViaSerializer, PaisSerializer, AutonomiaSerializer, ProvinciaSerializer, MunicipioSerializer
  
# http://www.django-rest-framework.org/api-guide/viewsets
# @action(permission_classes=[IsAuthenticated, IsAdminUser], methods=['GET'])
#@permission_classes((IsAuthenticated, IsAdminUser))

@permission_classes((permissions.IsAuthenticatedOrReadOnly, ))
class ViaViewSet(viewsets.ModelViewSet):
	queryset = Via.objects.all()
	serializer_class = ViaSerializer
	
@permission_classes((permissions.IsAuthenticatedOrReadOnly, ))
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

@api_view(['GET', 'POST'])
@permission_classes((permissions.IsAuthenticated, ))
def hello_world(request):
    return Response({"message": "Hello, world!"})

# new version
class ViaList(generics.ListCreateAPIView):
	model = Via
	serializer_class = ViaSerializer
	permission_classes = [permissions.AllowAny]

class ViaDetail(generics.RetrieveAPIView):
	model = Via
	serializer_class = ViaSerializer
	lookup_field = 'cod'