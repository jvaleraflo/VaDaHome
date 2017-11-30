# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-29 09:26
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='VGPIO',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('pin', models.PositiveSmallIntegerField()),
                ('nombre', models.CharField(max_length=50)),
            ],
            options={
                'ordering': ('pin',),
            },
        ),
    ]
