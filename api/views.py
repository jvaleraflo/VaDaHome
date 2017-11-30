# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from equipos.models import Equipo
from .serializers import EquipoSerializer
from bot.models import Bot
from .serializers import BotSerializer
from rest_framework import permissions

from rest_framework import generics


class EquipoList(generics.ListCreateAPIView):
    queryset = Equipo.objects.all()
    serializer_class = EquipoSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class BotList(generics.ListCreateAPIView):
    queryset = Bot.objects.all()
    serializer_class = BotSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class EquipoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Equipo.objects.all()
    serializer_class = EquipoSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class BotDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Bot.objects.all()
    serializer_class = BotSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
