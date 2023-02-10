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

@api_view(['GET','POST'])
def softDrinks(request):
    if request.method == 'GET':
        drinks = soft_drink.objects.all()
        serializer=SoftDrinkSerializer(drinks, many=True)
        return JsonResponse({'drinks':serializer.data})
    elif request.method == 'POST':
        serializer=SoftDrinkSerializer(data=request.GET)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

def AlcoholDrink(request):
    if request.method == 'GET':
        my_alcohol = alcohol.objects.all()
        serialized_alcohol=AlcoholSerializer(my_alcohol, many=True)
        return JsonResponse({'alcohols':serialized_alcohol.data})
    elif request.method == 'POST':
        my_alcohol =AlcoholSerializer(data=request.GET)
        if my_alcohol.is_valid():
            my_alcohol.save()
            return Response(my_alcohol.data, status=status.HTTP_201_CREATED)

def sodaDrink(request):
    sodas=soda.objects.all()
    serialized_sodas=SodaSerializer(sodas, many=True)
    return JsonResponse({'sodas':serialized_sodas.data})


