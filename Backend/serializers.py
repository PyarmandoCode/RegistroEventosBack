from rest_framework import serializers
from .models import Eventos, Cia, Empleados, Areas


class Eventos_serializer(serializers.ModelSerializer):
    class Meta:
        model = Eventos
        fields = '__all__'


class Cias_serializer(serializers.ModelSerializer):
    class Meta:
        model = Cia
        fields = '__all__'


class Areas_serializer(serializers.ModelSerializer):
    class Meta:
        model = Areas
        fields = '__all__'


class Empleados_serializer(serializers.ModelSerializer):
    class Meta:
        model = Empleados
        fields = '__all__'
