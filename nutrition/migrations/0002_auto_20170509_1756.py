# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nutrition', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='reslut',
            name='de1x',
            field=models.FloatField(default=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='reslut',
            name='mep',
            field=models.FloatField(default=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='reslut',
            name='nelp',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
    ]
