# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'UserProfile'
        db.create_table('jitterbunk_app_userprofile', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('photo', self.gf('django.db.models.fields.URLField')(max_length=200)),
        ))
        db.send_create_signal('jitterbunk_app', ['UserProfile'])

        # Adding model 'Bunk'
        db.create_table('jitterbunk_app_bunk', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('from_user', self.gf('django.db.models.fields.related.ForeignKey')(related_name='from_user', to=orm['jitterbunk_app.UserProfile'])),
            ('to_user', self.gf('django.db.models.fields.related.ForeignKey')(related_name='to_user', to=orm['jitterbunk_app.UserProfile'])),
            ('time', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal('jitterbunk_app', ['Bunk'])


    def backwards(self, orm):
        # Deleting model 'UserProfile'
        db.delete_table('jitterbunk_app_userprofile')

        # Deleting model 'Bunk'
        db.delete_table('jitterbunk_app_bunk')


    models = {
        'jitterbunk_app.bunk': {
            'Meta': {'object_name': 'Bunk'},
            'from_user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'from_user'", 'to': "orm['jitterbunk_app.UserProfile']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'time': ('django.db.models.fields.DateTimeField', [], {}),
            'to_user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'to_user'", 'to': "orm['jitterbunk_app.UserProfile']"})
        },
        'jitterbunk_app.userprofile': {
            'Meta': {'object_name': 'UserProfile'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'photo': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['jitterbunk_app']