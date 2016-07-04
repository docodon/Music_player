# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('musicplayer', '0002_auto_20160625_1401'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tracks',
            name='Rating',
            field=models.IntegerField(default=1, choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)]),
        ),
    ]
