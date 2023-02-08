from rest_framework import serializers
from .models import *

class SoftDrinkSerializer(serializers.modelSerializer):
    class Meta:
        model = soft_drink
        fields = ['Id','name','description']
