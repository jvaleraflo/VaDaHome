# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-24 08:07
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('equipos', '0005_auto_20171124_0800'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipo',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]