# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    operations = [
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('object_id', models.CharField(max_length=36, null=True)),
                ('event', models.CharField(max_length=50, db_index=True)),
                ('details', models.TextField(null=True)),
                ('timestamp', models.BigIntegerField(db_index=True)),
                ('content_type', models.ForeignKey(to='contenttypes.ContentType', null=True)),
            ],
            options={
                'ordering': ['-timestamp'],
            },
        ),
    ]
