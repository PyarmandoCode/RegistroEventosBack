from rest_framework import serializers
from .models import Customer,Eventos



class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['customer_id', 'lastname', 'firstname']


class Eventos_serializer(serializers.ModelSerializer):
    class Meta:
        model = Eventos
        fields = '__all__'
