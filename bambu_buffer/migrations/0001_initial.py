# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'BufferToken'
        db.create_table('buffer_token', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(related_name='buffer_tokens', unique=True, to=orm['auth.User'])),
            ('token', self.gf('django.db.models.fields.CharField')(max_length=36)),
        ))
        db.send_create_signal('bambu_buffer', ['BufferToken'])

        # Adding model 'BufferService'
        db.create_table('buffer_service', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('token', self.gf('django.db.models.fields.related.ForeignKey')(related_name='services', to=orm['bambu_buffer.BufferToken'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('remote_id', self.gf('django.db.models.fields.CharField')(max_length=36)),
            ('username', self.gf('django.db.models.fields.CharField')(max_length=30)),
        ))
        db.send_create_signal('bambu_buffer', ['BufferService'])

        # Adding model 'BufferProfile'
        db.create_table('buffer_profile', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('service', self.gf('django.db.models.fields.related.ForeignKey')(related_name='profiles', to=orm['bambu_buffer.BufferService'])),
            ('avatar', self.gf('django.db.models.fields.URLField')(max_length=255)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')()),
            ('default', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('formatted_username', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('remote_id', self.gf('django.db.models.fields.CharField')(unique=True, max_length=36)),
            ('schedules', self.gf('django.db.models.fields.TextField')()),
            ('selected', self.gf('django.db.models.fields.BooleanField')()),
        ))
        db.send_create_signal('bambu_buffer', ['BufferProfile'])

        # Adding model 'BufferedItem'
        db.create_table('buffer_buffereditem', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('content_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contenttypes.ContentType'])),
            ('object_id', self.gf('django.db.models.fields.PositiveIntegerField')()),
        ))
        db.send_create_signal('bambu_buffer', ['BufferedItem'])

        # Adding unique constraint on 'BufferedItem', fields ['content_type', 'object_id']
        db.create_unique('buffer_buffereditem', ['content_type_id', 'object_id'])


    def backwards(self, orm):
        # Removing unique constraint on 'BufferedItem', fields ['content_type', 'object_id']
        db.delete_unique('buffer_buffereditem', ['content_type_id', 'object_id'])

        # Deleting model 'BufferToken'
        db.delete_table('buffer_token')

        # Deleting model 'BufferService'
        db.delete_table('buffer_service')

        # Deleting model 'BufferProfile'
        db.delete_table('buffer_profile')

        # Deleting model 'BufferedItem'
        db.delete_table('buffer_buffereditem')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'bambu_buffer.buffereditem': {
            'Meta': {'unique_together': "(('content_type', 'object_id'),)", 'object_name': 'BufferedItem', 'db_table': "'buffer_buffereditem'"},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'object_id': ('django.db.models.fields.PositiveIntegerField', [], {})
        },
        'bambu_buffer.bufferprofile': {
            'Meta': {'object_name': 'BufferProfile', 'db_table': "'buffer_profile'"},
            'avatar': ('django.db.models.fields.URLField', [], {'max_length': '255'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {}),
            'default': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'formatted_username': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'remote_id': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '36'}),
            'schedules': ('django.db.models.fields.TextField', [], {}),
            'selected': ('django.db.models.fields.BooleanField', [], {}),
            'service': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'profiles'", 'to': "orm['bambu_buffer.BufferService']"})
        },
        'bambu_buffer.bufferservice': {
            'Meta': {'object_name': 'BufferService', 'db_table': "'buffer_service'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'remote_id': ('django.db.models.fields.CharField', [], {'max_length': '36'}),
            'token': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'services'", 'to': "orm['bambu_buffer.BufferToken']"}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        'bambu_buffer.buffertoken': {
            'Meta': {'object_name': 'BufferToken', 'db_table': "'buffer_token'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'token': ('django.db.models.fields.CharField', [], {'max_length': '36'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'buffer_tokens'", 'unique': 'True', 'to': u"orm['auth.User']"})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['bambu_buffer']