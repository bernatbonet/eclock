# -*- encoding: utf-8 -*-
#from django.shortcuts import render
from rest_framework import viewsets
from models import Cnae, Sujeto, Sector, SituacionProcesal, Persona
from serializers import CnaeSerializer, SujetoSerializer, SectorSerializer, SituacionProcesalSerializer, PersonaSerializer

class CnaeViewSet(viewsets.ModelViewSet):
	queryset = Cnae.objects.all()
	serializer_class = CnaeSerializer

class SujetoViewSet(viewsets.ModelViewSet):
	queryset = Sujeto.objects.all()
	serializer_class = SujetoSerializer

class SectorViewSet(viewsets.ModelViewSet):
	queryset = Sector.objects.all()
	serializer_class = SectorSerializer

class SituacionProcesalViewSet(viewsets.ModelViewSet):
	queryset = SituacionProcesal.objects.all()
	serializer_class = SituacionProcesalSerializer

class PersonaViewSet(viewsets.ModelViewSet):
	queryset = Persona.objects.all()
	serializer_class = PersonaSerializer