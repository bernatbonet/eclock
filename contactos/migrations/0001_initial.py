# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Cnae'
        db.create_table(u'contactos_cnae', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('cod', self.gf('django.db.models.fields.CharField')(unique=True, max_length=4)),
            ('nom', self.gf('django.db.models.fields.CharField')(unique=True, max_length=100)),
        ))
        db.send_create_signal(u'contactos', ['Cnae'])

        # Adding model 'Sujeto'
        db.create_table(u'contactos_sujeto', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('cod', self.gf('django.db.models.fields.CharField')(unique=True, max_length=2)),
            ('nom', self.gf('django.db.models.fields.CharField')(unique=True, max_length=100)),
            ('sufijo', self.gf('django.db.models.fields.CharField')(max_length=2, null=True, blank=True)),
        ))
        db.send_create_signal(u'contactos', ['Sujeto'])

        # Adding model 'Sector'
        db.create_table(u'contactos_sector', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('cod', self.gf('django.db.models.fields.CharField')(unique=True, max_length=2)),
            ('nom', self.gf('django.db.models.fields.CharField')(unique=True, max_length=100)),
            ('formasolcial', self.gf('django.db.models.fields.CharField')(max_length=4, null=True, blank=True)),
        ))
        db.send_create_signal(u'contactos', ['Sector'])

        # Adding model 'SituacionProcesal'
        db.create_table(u'contactos_situacionprocesal', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('cod', self.gf('django.db.models.fields.CharField')(unique=True, max_length=2)),
            ('nom', self.gf('django.db.models.fields.CharField')(unique=True, max_length=100)),
        ))
        db.send_create_signal(u'contactos', ['SituacionProcesal'])

        # Adding model 'Persona'
        db.create_table(u'contactos_persona', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('cifespanol', self.gf('django.db.models.fields.CharField')(unique=True, max_length=9)),
            ('cifeuropeo', self.gf('django.db.models.fields.CharField')(max_length=15, null=True, blank=True)),
            ('nom', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('codvia', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ubicaciones.Via'], null=True, blank=True)),
            ('via', self.gf('django.db.models.fields.CharField')(unique=True, max_length=35)),
            ('calle', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('numero1', self.gf('django.db.models.fields.CharField')(max_length=5)),
            ('numero2', self.gf('django.db.models.fields.CharField')(max_length=5, null=True, blank=True)),
            ('escalera', self.gf('django.db.models.fields.CharField')(max_length=2, null=True, blank=True)),
            ('piso', self.gf('django.db.models.fields.CharField')(max_length=5, null=True, blank=True)),
            ('puerta', self.gf('django.db.models.fields.CharField')(max_length=5, null=True, blank=True)),
            ('letra', self.gf('django.db.models.fields.CharField')(max_length=2, null=True, blank=True)),
            ('codigopostal', self.gf('django.db.models.fields.CharField')(max_length=8, null=True, blank=True)),
            ('codpais', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ubicaciones.Pais'], null=True, blank=True)),
            ('pais', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('codprovincia', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ubicaciones.Provincia'], null=True, blank=True)),
            ('provincia', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('codmunicipio', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ubicaciones.Municipio'], null=True, blank=True)),
            ('municipio', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('telefono', self.gf('django.db.models.fields.CharField')(max_length=15, null=True, blank=True)),
            ('telefono2', self.gf('django.db.models.fields.CharField')(max_length=15, null=True, blank=True)),
            ('telefono3', self.gf('django.db.models.fields.CharField')(max_length=15, null=True, blank=True)),
            ('movil', self.gf('django.db.models.fields.CharField')(max_length=15, null=True, blank=True)),
            ('movil2', self.gf('django.db.models.fields.CharField')(max_length=15, null=True, blank=True)),
            ('movil3', self.gf('django.db.models.fields.CharField')(max_length=15, null=True, blank=True)),
            ('fax', self.gf('django.db.models.fields.CharField')(max_length=15, null=True, blank=True)),
            ('fax2', self.gf('django.db.models.fields.CharField')(max_length=15, null=True, blank=True)),
            ('fax3', self.gf('django.db.models.fields.CharField')(max_length=15, null=True, blank=True)),
            ('email', self.gf('django.db.models.fields.CharField')(max_length=250, null=True, blank=True)),
            ('email2', self.gf('django.db.models.fields.CharField')(max_length=250, null=True, blank=True)),
            ('email3', self.gf('django.db.models.fields.CharField')(max_length=250, null=True, blank=True)),
            ('sujeto', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contactos.Sujeto'], null=True, blank=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('apellidos', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('cnae', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contactos.Cnae'], null=True, blank=True)),
            ('sector', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contactos.Sector'], null=True, blank=True)),
            ('situacionprocesal', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contactos.SituacionProcesal'], null=True, blank=True)),
            ('altocargo', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('residente', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('fechanacimiento', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'contactos', ['Persona'])


    def backwards(self, orm):
        # Deleting model 'Cnae'
        db.delete_table(u'contactos_cnae')

        # Deleting model 'Sujeto'
        db.delete_table(u'contactos_sujeto')

        # Deleting model 'Sector'
        db.delete_table(u'contactos_sector')

        # Deleting model 'SituacionProcesal'
        db.delete_table(u'contactos_situacionprocesal')

        # Deleting model 'Persona'
        db.delete_table(u'contactos_persona')


    models = {
        u'contactos.cnae': {
            'Meta': {'object_name': 'Cnae'},
            'cod': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '4'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nom': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'})
        },
        u'contactos.persona': {
            'Meta': {'object_name': 'Persona'},
            'altocargo': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'apellidos': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'calle': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'cifespanol': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '9'}),
            'cifeuropeo': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            'cnae': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contactos.Cnae']", 'null': 'True', 'blank': 'True'}),
            'codigopostal': ('django.db.models.fields.CharField', [], {'max_length': '8', 'null': 'True', 'blank': 'True'}),
            'codmunicipio': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ubicaciones.Municipio']", 'null': 'True', 'blank': 'True'}),
            'codpais': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ubicaciones.Pais']", 'null': 'True', 'blank': 'True'}),
            'codprovincia': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ubicaciones.Provincia']", 'null': 'True', 'blank': 'True'}),
            'codvia': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ubicaciones.Via']", 'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'email2': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'email3': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'escalera': ('django.db.models.fields.CharField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'fax': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            'fax2': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            'fax3': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            'fechanacimiento': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'letra': ('django.db.models.fields.CharField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'movil': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            'movil2': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            'movil3': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            'municipio': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'nom': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'numero1': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'numero2': ('django.db.models.fields.CharField', [], {'max_length': '5', 'null': 'True', 'blank': 'True'}),
            'pais': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'piso': ('django.db.models.fields.CharField', [], {'max_length': '5', 'null': 'True', 'blank': 'True'}),
            'provincia': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'puerta': ('django.db.models.fields.CharField', [], {'max_length': '5', 'null': 'True', 'blank': 'True'}),
            'residente': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'sector': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contactos.Sector']", 'null': 'True', 'blank': 'True'}),
            'situacionprocesal': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contactos.SituacionProcesal']", 'null': 'True', 'blank': 'True'}),
            'sujeto': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contactos.Sujeto']", 'null': 'True', 'blank': 'True'}),
            'telefono': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            'telefono2': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            'telefono3': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            'via': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '35'})
        },
        u'contactos.sector': {
            'Meta': {'object_name': 'Sector'},
            'cod': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '2'}),
            'formasolcial': ('django.db.models.fields.CharField', [], {'max_length': '4', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nom': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'})
        },
        u'contactos.situacionprocesal': {
            'Meta': {'object_name': 'SituacionProcesal'},
            'cod': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '2'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nom': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'})
        },
        u'contactos.sujeto': {
            'Meta': {'object_name': 'Sujeto'},
            'cod': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '2'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nom': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'sufijo': ('django.db.models.fields.CharField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'})
        },
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
            'fechacee': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
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

    complete_apps = ['contactos']