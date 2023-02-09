from django.shortcuts import render
from .models import *
from django.http import JsonResponse
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
# Get all drinks
#Serialize them
#Retun json

@api_view('GET','POST')
def softDrinks(request):
    if request.method == 'GET':
        drinks = soft_drink.objects.all()
        serialized_data=SoftDrinkSerializer(drinks, many=True)
        return JsonResponse({'drinks':serialized_data.data})
    if request.method == 'POST':
        serialize_data=SoftDrinkSerializer(data=request.data)
        if serialize_data.is_valid():
            serialize_data.save()
            return Response(serialize_data.data, status=status.HTTP_201_CREATED)

def AlcoholDrink(request):
    my_alcohol = alcohol.objects.all()
    serialized_alcohol=AlcoholSerializer(my_alcohol, many=True)
    return JsonResponse({'alcohols':serialized_alcohol.data})

def sodaDrink(request):
    sodas=soda.objects.all()
    serialized_sodas=SodaSerializer(sodas, many=True)
    return JsonResponse({'sodas':serialized_sodas.data})


