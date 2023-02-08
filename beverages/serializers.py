from rest_framework import serializers
from .models import *

class SoftDrinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = soft_drink
        fields = ['id','name','description']

class AlcoholSerializer(serializers.ModelSerializer):
    class Meta:
        model = alcohol
        fields = ['id','name','description']