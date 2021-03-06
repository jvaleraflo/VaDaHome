# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-22 12:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Equipos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('ip', models.GenericIPAddressField()),
                ('mac', models.CharField(max_length=17)),
                ('tipo', models.CharField(choices=[('ordenador', 'Ordenador'), ('camara', 'Camara')], max_length=50)),
            ],
        ),
    ]
