# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Pais.fechacee'
        db.alter_column(u'ubicaciones_pais', 'fechacee', self.gf('django.db.models.fields.DateField')(null=True))

    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'Pais.fechacee'
        raise RuntimeError("Cannot reverse this migration. 'Pais.fechacee' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration
        # Changing field 'Pais.fechacee'
        db.alter_column(u'ubicaciones_pais', 'fechacee', self.gf('django.db.models.fields.DateField')())

    models = {
        u'ubicaciones.autonomia': {
            'Meta': {'object_name': 'Autonomia'},
            'cod': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '3'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nom': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'})
        },
        u'ubicaciones.municipio': {
            'Meta': {'object_name': 'Municipio'},
            'autonomia': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ubicaciones.Autonomia']", 'blank': 'True'}),
            'cod': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '5'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nom': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'}),
            'pais': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ubicaciones.Pais']"}),
            'provincia': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ubicaciones.Provincia']", 'blank': 'True'})
        },
        u'ubicaciones.pais': {
            'Meta': {'object_name': 'Pais'},
            'cee': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'cod': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '3'}),
            'cod347': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '3'}),
            'codiso': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '3'}),
            'fechacee': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nom': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'sigla': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'})
        },
        u'ubicaciones.provincia': {
            'Meta': {'object_name': 'Provincia'},
            'autonomia': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ubicaciones.Autonomia']", 'blank': 'True'}),
            'cod': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '2'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nom': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'pais': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ubicaciones.Pais']"})
        },
        u'ubicaciones.via': {
            'Meta': {'object_name': 'Via'},
            'cod': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '5'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nom': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '35'})
        }
    }

    complete_apps = ['ubicaciones']