# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('musicplayer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Genre_id',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Genre_name', models.CharField(max_length=100)),
                ('Genre_id', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Id_genre',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Genre_name', models.CharField(max_length=100)),
                ('Genre_id', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='tracks',
            name='Track',
            field=models.FileField(upload_to=b'tracks'),
        ),
    ]
