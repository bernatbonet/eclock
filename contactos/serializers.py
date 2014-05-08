#-*- coding: utf-8 -*-
from django.db.models.signals import pre_save
from models import Cnae, Sujeto, Sector, SituacionProcesal, Persona
from rest_framework import serializers

class CnaeSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Cnae
		fields = ('cod', 'nom', )

class SujetoSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Sujeto
		fields = ('cod', 'nom', 'formasocial', )

class SectorSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Sector
		fields = ('cod', 'nom', 'sufijo', )

	def pre_save(self, obj):
		print 'pre-save'
		print self.object.cod

	def save(self, *args, **kwargs):
		print 'save'
		if (self.object.sufijo is None) or (self.object.sufijo==""):
			self.object.sufijo = self.object.cod
		print ('sufijo post: %s') %(self.object.sufijo)
		pass

class SituacionProcesalSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = SituacionProcesal
		fields = ('cod', 'nom', )

class PersonaSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Persona
		fields = ('cifespanol', 'cifeuropeo', 'nom', 'codvia', 'via', 'calle', 'numero1', 'numero2', 'escalera', 'piso', 'puerta', 'letra', 'codigopostal', 'codpais', 'pais', 'codprovincia', 'provincia', 'codmunicipio', 'municipio', 'telefono', 'telefono2', 'telefono3', 'movil', 'movil2', 'movil3', 'fax', 'fax2', 'fax3', 'email', 'email2', 'email3', 'sujeto', 'nombre', 'apellidos', 'cnae', 'sector', 'situacionprocesal', 'altocargo', 'residente', 'fechanacimiento', )