from django.shortcuts import render
from .models import *
from django.http import JsonResponse
from .serializers import *

# Get all drinks
#Serialize them
#Retun json
def softDrinks(request):
    drinks = soft_drink.objects.all()
    serialized_data=SoftDrinkSerializer(drinks, many=True)
    return JsonResponse({'drinks':serialized_data.data})

def AlcoholDrink(request):
    my_alcohol = alcohol.objects.all()
    serialized_alcohol=AlcoholSerializer(my_alcohol, many=True)
    return JsonResponse({'alcohols':serialized_alcohol.data})

def sodaDrink(request):
    sodas=soda.objects.all()
    serialized_sodas=SodaSerializer(sodas, many=True)
    return JsonResponse({'sodas':serialized_sodas.data})


