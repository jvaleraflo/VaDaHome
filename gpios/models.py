# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import uuid

from django.db import models


# Create your models here.

"""
# Diccionario con los gpios a utilizar:
pins = {
    17: {'name': 'Disco duro externo', 'state': GPIO.HIGH},
    18: {'name': 'Internet de Adrian', 'state': GPIO.HIGH}
}
"""


class VGPIO(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    pin = models.PositiveSmallIntegerField()
    nombre = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre

    class Meta:
        ordering = ('pin',)

