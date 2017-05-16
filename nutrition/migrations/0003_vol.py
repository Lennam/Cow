# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nutrition', '0002_auto_20170509_1756'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vol',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField()),
                ('volOne', models.FloatField()),
                ('volTwo', models.FloatField()),
                ('volThree', models.FloatField()),
                ('volFour', models.FloatField()),
                ('volFive', models.FloatField()),
            ],
        ),
    ]
