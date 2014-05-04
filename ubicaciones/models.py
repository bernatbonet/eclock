#-*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.
class Meta:
	verbose_name = _(u'Ubicación')
	verbose_name_plural = _(u'Ubicaciones')

class Via(models.Model):
	cod  = models.CharField(max_length=5, verbose_name=_(u'Código'), help_text=_(u'Introduzca el código'), unique=True)
	nom = models.CharField(max_length=35, verbose_name=_(u'Nombre'), help_text=_(u'Introduzca el nombre de la vía'), unique=True)

	def __unicode__(self):
		return self.nom

	class Meta:
		verbose_name = _(u'Via')
		verbose_name_plural = _(u'Vías')

class Pais(models.Model):
	cod = models.CharField(max_length=3, verbose_name=_(u'Código'), help_text=_(u'Introduzca el código'), unique=True)
	cod347 = models.CharField(max_length=3, verbose_name=_(u'Código 347'), help_text=_(u'Introduzca el código 347'), unique=True)
	codiso = models.CharField(max_length=3, verbose_name=_(u'Código ISO'), help_text=_(u'Introduzca el código iso'), unique=True)
	nom = models.CharField(max_length=100, verbose_name=_(u'Nombre'), help_text=_(u'Introduzca el nombre'), unique=True)
	sigla = models.CharField(max_length=100, verbose_name=_(u'Sigla'), help_text=_(u'Introduzca las siglas'), unique=True)
	cee = models.BooleanField(default=True, verbose_name=_(u'CEE'), help_text=_(u'Introduzca si pertenece a la CEE'))
	fechacee = models.DateField(verbose_name=_(u'Fecha Ingreso CEE'), help_text=_(u'Introduzca la fecha de ingreso en la CEE'), null=True, blank=True)

	def __unicode__(self):
		return self.nom

	class Meta:
		verbose_name = _(u'País')
		verbose_name_plural = _(u'Paises')

class Autonomia(models.Model):
	cod = models.CharField(max_length=3, verbose_name=_(u'Código'), help_text=_(u'Introduzca el código'), unique=True)
	nom = models.CharField(max_length=100, verbose_name=_(u'Nombre'), help_text=_(u'Introduzca el nombre'), unique=True)

	def __unicode__(self):
		return self.nom

	class Meta:
		verbose_name = _(u'Autonomía')
		verbose_name_plural = _(u'Autonomias')

class Provincia(models.Model):
	pais = models.ForeignKey(Pais, verbose_name=_(u'País'), help_text=_(u'Introduzca el país'), blank=False)
	autonomia = models.ForeignKey(Autonomia, verbose_name=_(u'Autonomía'), help_text=_(u'Introduzca la autonomía'), blank=True)
	cod =  models.CharField(max_length=2, verbose_name=_(u'Código'), help_text=_(u'Introduzca el código'), unique=True)
	nom = models.CharField(max_length=100, verbose_name=_(u'Nombre'), help_text=_(u'Introduzca el nombre'), unique=True)

	def __unicode__(self):
		return self.nom

	class Meta:
		verbose_name = _(u'Provincia')
		verbose_name_plural = _(u'Provincias')

class Municipio(models.Model):
	pais = models.ForeignKey(Pais, verbose_name=_(u'País'), help_text=_(u'Introduzca el país'), blank=False)
	autonomia = models.ForeignKey(Autonomia, verbose_name=_(u'Autonomía'), help_text=_(u'Introduzca la autonomía'), blank=True)
	provincia = models.ForeignKey(Provincia, verbose_name=_(u'Provincia'), help_text=_(u'Introduzca la provincia'), blank=True)
	cod = models.CharField(max_length=5, verbose_name=_(u'Código'), help_text=_(u'Introduzca el código'), unique=True)
	nom = models.CharField(max_length=50, verbose_name=_(u'Nombre'), help_text=_(u'Introduzca el nombre'),  unique=True)

	def __unicode__(self):
		return self.nom

	class Meta:
		verbose_name = _(u'Municipio')
		verbose_name_plural = _(u'Municipios')
