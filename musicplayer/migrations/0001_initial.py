# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tracks',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Track_name', models.CharField(max_length=100)),
                ('Genre_id', models.IntegerField()),
                ('Track_title', models.CharField(max_length=100)),
                ('Rating', models.IntegerField()),
                ('Track', models.FileField(upload_to=b'')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
