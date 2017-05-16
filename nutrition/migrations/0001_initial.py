# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fodder',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField()),
                ('nameOne', models.CharField(max_length=30)),
                ('nameTwo', models.CharField(max_length=30)),
                ('nameThree', models.CharField(max_length=30)),
                ('nameFour', models.CharField(max_length=30)),
                ('nameFive', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Reslut',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField()),
                ('tdnfc', models.FloatField()),
                ('tdcpf', models.FloatField()),
                ('tdcpc', models.FloatField()),
                ('tdfa', models.FloatField()),
                ('tdndf', models.FloatField()),
                ('tdn', models.FloatField()),
            ],
        ),
    ]
