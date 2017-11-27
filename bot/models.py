# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import uuid
from django.db import models


class Bot(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nombre = models.CharField(max_length=50)
    token = models.CharField(max_length=100, default='')
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre