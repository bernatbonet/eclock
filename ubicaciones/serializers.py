#-*- coding: utf-8 -*-
from models import Via, Pais, Autonomia, Provincia, Municipio
from rest_framework import serializers

class ViaSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Via
		fields = ('cod', 'nom', )

class PaisSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Pais
		fields = ('cod', 'cod347', 'codiso', 'nom', 'sigla', 'cee', 'fechacee', )

class AutonomiaSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Autonomia
		fields = ('cod', 'nom', )

class ProvinciaSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Provincia
		fields = ('pais', 'autonomia', 'cod', 'nom', )

class MunicipioSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Municipio
		fields = ('pais', 'autonomia', 'provincia', 'cod', 'nom', )