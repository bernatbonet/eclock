# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Via'
        db.create_table(u'ubicaciones_via', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('cod', self.gf('django.db.models.fields.CharField')(unique=True, max_length=5)),
            ('nom', self.gf('django.db.models.fields.CharField')(unique=True, max_length=35)),
        ))
        db.send_create_signal(u'ubicaciones', ['Via'])

        # Adding model 'Pais'
        db.create_table(u'ubicaciones_pais', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('cod', self.gf('django.db.models.fields.CharField')(unique=True, max_length=3)),
            ('cod347', self.gf('django.db.models.fields.CharField')(unique=True, max_length=3)),
            ('codiso', self.gf('django.db.models.fields.CharField')(unique=True, max_length=3)),
            ('nom', self.gf('django.db.models.fields.CharField')(unique=True, max_length=100)),
            ('sigla', self.gf('django.db.models.fields.CharField')(unique=True, max_length=100)),
            ('cee', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('fechacee', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal(u'ubicaciones', ['Pais'])

        # Adding model 'Autonomia'
        db.create_table(u'ubicaciones_autonomia', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('cod', self.gf('django.db.models.fields.CharField')(unique=True, max_length=3)),
            ('nom', self.gf('django.db.models.fields.CharField')(unique=True, max_length=100)),
        ))
        db.send_create_signal(u'ubicaciones', ['Autonomia'])

        # Adding model 'Provincia'
        db.create_table(u'ubicaciones_provincia', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('pais', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ubicaciones.Pais'])),
            ('autonomia', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ubicaciones.Autonomia'], blank=True)),
            ('cod', self.gf('django.db.models.fields.CharField')(unique=True, max_length=2)),
            ('nom', self.gf('django.db.models.fields.CharField')(unique=True, max_length=100)),
        ))
        db.send_create_signal(u'ubicaciones', ['Provincia'])

        # Adding model 'Municipio'
        db.create_table(u'ubicaciones_municipio', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('pais', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ubicaciones.Pais'])),
            ('autonomia', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ubicaciones.Autonomia'], blank=True)),
            ('provincia', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ubicaciones.Provincia'], blank=True)),
            ('cod', self.gf('django.db.models.fields.CharField')(unique=True, max_length=5)),
            ('nom', self.gf('django.db.models.fields.CharField')(unique=True, max_length=50)),
        ))
        db.send_create_signal(u'ubicaciones', ['Municipio'])


    def backwards(self, orm):
        # Deleting model 'Via'
        db.delete_table(u'ubicaciones_via')

        # Deleting model 'Pais'
        db.delete_table(u'ubicaciones_pais')

        # Deleting model 'Autonomia'
        db.delete_table(u'ubicaciones_autonomia')

        # Deleting model 'Provincia'
        db.delete_table(u'ubicaciones_provincia')

        # Deleting model 'Municipio'
        db.delete_table(u'ubicaciones_municipio')


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
            'fechacee': ('django.db.models.fields.DateField', [], {}),
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