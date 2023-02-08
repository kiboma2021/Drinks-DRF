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
    return JsonResponse(serialized_data.data, safe=False)

def AlcoholDrink(request):
    my_alcohol = alcohol.objects.all()
    serialized_alcohol=AlcoholSerializer(my_alcohol, many=True)
    return JsonResponse(serialized_alcohol.data, safe=False)


