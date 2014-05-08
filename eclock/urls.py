# -*- encoding: utf-8 -*-
from django.conf.urls import include, patterns, url
from rest_framework import routers

from ubicaciones.views import ViaViewSet, PaisViewSet, AutonomiaViewSet, ProvinciaViewSet, MunicipioViewSet, hello_world
from contactos.views import CnaeViewSet, SujetoViewSet, SectorViewSet, SituacionProcesalViewSet, PersonaViewSet

router = routers.DefaultRouter()
router.register(r'vias', ViaViewSet)
router.register(r'paises', PaisViewSet)
router.register(r'autonomias', AutonomiaViewSet)
router.register(r'provincias', ProvinciaViewSet)
router.register(r'municipios', MunicipioViewSet)
router.register(r'cnaes', CnaeViewSet)
router.register(r'sujetos', SujetoViewSet)
router.register(r'sectores', SectorViewSet)
router.register(r'situacionesprocesal', SituacionProcesalViewSet)
router.register(r'personas', PersonaViewSet)

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^', include(router.urls)),
    url(r'^hello/', hello_world),
	url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^admin/', include(admin.site.urls)),
)
