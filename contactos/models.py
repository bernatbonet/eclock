#-*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _

from ubicaciones.models import Via, Pais, Provincia, Municipio

# OJO: unique_together = ('field1','field2')

# Create your models here.
class Meta:
	verbose_name = _(u'Contacto')
	verbose_name_plural = _(u'Contactos')

class Cnae(models.Model):
	cod = models.CharField(max_length=4, verbose_name=_(u'Código'), help_text=_(u'Introduzca el código'), unique=True)
	nom = models.CharField(max_length=100, verbose_name=_(u'Nombre'), help_text=_(u'Introduzca el nombre'), unique=True)

	def __unicode__(self):
		return self.nom

	class Meta:
		verbose_name = _(u'Cnae')
		verbose_name_plural = _(u'Cnae')

class Sujeto(models.Model):
	cod = models.CharField(max_length=3, verbose_name=_(u'Código'), help_text=_(u'Introduzca el código'), unique=True)
	nom = models.CharField(max_length=100, verbose_name=_(u'Nombre'), help_text=_(u'Introduzca el nombre'), unique=True)
	formasocial = models.CharField(max_length=10, verbose_name=_(u'Forma Social'), help_text=_(u'Introduzca la forma social'), null=True, blank=True)

	def __unicode__(self):
		return self.nom

	class Meta:
		verbose_name = _(u'Sujeto')
		verbose_name_plural = _(u'Sujetos')

class Sector(models.Model):
	cod = models.CharField(max_length=2, verbose_name=_(u'Código'), help_text=_(u'Introduzca el código'), unique=True)
	nom = models.CharField(max_length=100, verbose_name=_(u'Nombre'), help_text=_(u'Introduzca el nombre'), unique=True)
	sufijo = models.CharField(max_length=4, verbose_name=_(u'Sufijo'), help_text=_(u'Introduzca el sufijo'), null=True, blank=True)

	def __unicode__(self):
		return self.nom

	class Meta:
		verbose_name = _(u'Sujeto')
		verbose_name_plural = _(u'Sujetos')

class SituacionProcesal(models.Model):
	cod = models.CharField(max_length=2, verbose_name=_(u'Código'), help_text=_(u'Introduzca el código'), unique=True)
	nom = models.CharField(max_length=100, verbose_name=_(u'Nombre'), help_text=_(u'Introduzca el nombre'), unique=True)

	def __unicode__(self):
		return self.nom

	class Meta:
		verbose_name = _(u'Sujeto')
		verbose_name_plural = _(u'Sujetos')

class Persona(models.Model):
	cifespanol = models.CharField(max_length=9, verbose_name=_(u'Cif/Dni Español'), help_text=_(u'Introduzca el cif/dni español'), unique=True)
	cifeuropeo = models.CharField(max_length=15, verbose_name=_(u'Cif/Dni Europeo'), help_text=_(u'Introduzca el cif/dni europeo'), null=True, blank=True)
	nom = models.CharField(max_length=100, verbose_name=_(u'Nombre'), help_text=_(u'Introduzca el nombre'))
	codvia =  models.ForeignKey(Via, verbose_name=_(u'Vía'), help_text=_(u'Introduzca la vía'), null=True, blank=True)
	via = models.CharField(max_length=35, verbose_name=_(u'Vía'), help_text=_(u'Introduzca la vía'))
	calle = models.CharField(max_length=100, verbose_name=_(u'Nombre Vía'), help_text=_(u'Introduzca el nombre de la vía'))
	numero1 = models.CharField(max_length=5, verbose_name=_(u'Número'), help_text=_(u'Introduzca el número'))
	numero2 = models.CharField(max_length=5, verbose_name=_(u'Número 2'), help_text=_(u'Introduzca el número 2'), null=True, blank=True)
	escalera = models.CharField(max_length=2, verbose_name=_(u'Escalera'), help_text=_(u'Introduzca la escalera'), null=True, blank=True)
	piso = models.CharField(max_length=5, verbose_name=_(u'Piso'), help_text=_(u'Introduzca el piso'), null=True, blank=True)
	puerta = models.CharField(max_length=5, verbose_name=_(u'Puerta'), help_text=_(u'Introduzca la puerta'), null=True, blank=True)
	letra = models.CharField(max_length=2, verbose_name=_(u'Letra'), help_text=_(u'Introduzca la letra'), null=True, blank=True)
	codigopostal = models.CharField(max_length=8, verbose_name=_(u'Código Postal'), help_text=_(u'Introduzca el códgo postal'), null=True, blank=True)
	codpais =  models.ForeignKey(Pais, verbose_name=_(u'País'), help_text=_(u'Introduzca el país'), null=True, blank=True)
	pais = models.CharField(max_length=100, verbose_name=_(u'País'), help_text=_(u'Introduzca el país'), null=True, blank=True)
	codprovincia =  models.ForeignKey(Provincia, verbose_name=_(u'Provincia'), help_text=_(u'Introduzca la provincia'), null=True, blank=True)
	provincia = models.CharField(max_length=100, verbose_name=_(u'Provincia'), help_text=_(u'Introduzca la provincia'), null=True, blank=True)
	codmunicipio = models.ForeignKey(Municipio, verbose_name=_(u'Municipio'), help_text=_(u'Introduzca el municipio'), null=True, blank=True)
	municipio = models.CharField(max_length=100, verbose_name=_(u'Municipio'), help_text=_(u'Introduzca el municipio'), null=True, blank=True)
	telefono = models.CharField(max_length=15, verbose_name=_(u'Teléfono'), help_text=_(u'Introduzca el teléfono'), null=True, blank=True)
	telefono2 = models.CharField(max_length=15, verbose_name=_(u'Teléfono 2'), help_text=_(u'Introduzca el teléfono 2'), null=True, blank=True)
	telefono3 = models.CharField(max_length=15, verbose_name=_(u'Teléfono 3'), help_text=_(u'Introduzca el teléfono 3'), null=True, blank=True)
	movil = models.CharField(max_length=15, verbose_name=_(u'Móvil'), help_text=_(u'Introduzca el móvil'), null=True, blank=True)
	movil2 = models.CharField(max_length=15, verbose_name=_(u'Móvil 2'), help_text=_(u'Introduzca el móvil 2'), null=True, blank=True)
	movil3 = models.CharField(max_length=15, verbose_name=_(u'Móvil 3'), help_text=_(u'Introduzca el móvil 3'), null=True, blank=True)
	fax = models.CharField(max_length=15, verbose_name=_(u'Fax'), help_text=_(u'Introduzca el fax'), null=True, blank=True)
	fax2 = models.CharField(max_length=15, verbose_name=_(u'Fax 2'), help_text=_(u'Introduzca el fax 2'), null=True, blank=True)
	fax3 = models.CharField(max_length=15, verbose_name=_(u'Fax 3'), help_text=_(u'Introduzca el fax 3'), null=True, blank=True)
	email = models.CharField(max_length=250, verbose_name=_(u'Email'), help_text=_(u'Introduzca el email'), null=True, blank=True)
	email2 = models.CharField(max_length=250, verbose_name=_(u'Email 2'), help_text=_(u'Introduzca el email 2'), null=True, blank=True)
	email3 = models.CharField(max_length=250, verbose_name=_(u'Email 3'), help_text=_(u'Introduzca el email 3'), null=True, blank=True)
	sujeto = models.ForeignKey(Sujeto, verbose_name=_(u'Sujeto'), help_text=_(u'Introduzca el sujeto'), null=True, blank=True)
	nombre = models.CharField(max_length=100, verbose_name=_(u'Nombre'), help_text=_(u'Introduzca el nombre'), null=True, blank=True)
	apellidos = models.CharField(max_length=100, verbose_name=_(u'Apellidos'), help_text=_(u'Introduzca los apellidos'), null=True, blank=True)
	cnae = models.ForeignKey(Cnae, verbose_name=_(u'Cnae'), help_text=_(u'Introduzca el cnae'), null=True, blank=True)
	sector = models.ForeignKey(Sector, verbose_name=_(u'Sector'), help_text=_(u'Introduzca el sector'), null=True, blank=True)
	situacionprocesal = models.ForeignKey(SituacionProcesal, verbose_name=_(u'Sitación Procesal'), help_text=_(u'Introduzca la situación procesal'), null=True, blank=True)
	altocargo = models.BooleanField(default=False, verbose_name=_(u'Alto Cargo'), help_text=_(u'Introduzca si es alto cargo'))
	residente = models.BooleanField(default=True, verbose_name=_(u'Residente'), help_text=_(u'Introduzca si es residente'))
	fechanacimiento = models.DateField(verbose_name=_(u'Fecha de Nacimiento'), help_text=_(u'Introduzca la fecha de nacimiento'), null=True, blank=True)
	#iban = models.CharField(max_length=100, verbose_name=_(u'IBAN'), help_text=_(u'Introduzca la cuenta IBAN'), null=True, blank=True)
	#idioma = models.ForeignKey(Idioma, verbose_name=_(u'Idioma'), help_text=_(u'Introduzca el idioma'), null=True, blank=True)

	def __unicode__(self):
		return self.nom

	class Meta:
		verbose_name = _(u'Persona')
		verbose_name_plural = _(u'Personas')
