# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import uuid

from django.db import models


# Create your models here.

"""
equipos = {
    1: {'estado': 'indeterminado', 'nombre': 'cdavila-pc', 'ip': '192.168.2.30', 'mac': '00:1e:8c:67:d6:2d', 'espera': 10},
    2: {'estado': 'indeterminado', 'nombre': 'peliculas-pc', 'ip': '192.168.2.60', 'mac': '00:01:2e:bc:30:dd', 'espera': 12}
}
"""

class Equipo(models.Model):

    ORDENADOR = 'ord'
    CAMARA = 'cam'

    TIPOS_DISPONIBLES = (
        (ORDENADOR, 'Ordenador'),
        (CAMARA, 'Camara'),
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nombre = models.CharField(max_length=50)
    ip = models.GenericIPAddressField()
    mac = models.CharField(max_length=17)
    tipo = models.CharField(max_length=50, choices=TIPOS_DISPONIBLES)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)



    def __str__(self):
        return self.nombre

    class Meta:
        ordering = ('tipo',)