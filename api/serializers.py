from rest_framework import serializers

from equipos.models import Equipo
from bot.models import Bot
from gpios.models import VGPIO


class EquipoSerializer (serializers.ModelSerializer):
    class Meta:
        model = Equipo
        fields = ('id', 'nombre', 'ip', 'mac', 'tipo', 'created_at', 'modified_at')


class BotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bot
        fields = ('id', 'nombre', 'token', 'created_at', 'modified_at')


class GPIOSerializer(serializers.ModelSerializer):
    class Meta:
        model = VGPIO
        fields = ('id', 'pin', 'nombre', 'created_at', 'modified_at')