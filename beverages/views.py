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
    try:
        drinks = soft_drink.objects.all()
    except soft_drink.DoesNotExist:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'GET':
        serializer=SoftDrinkSerializer(drinks, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer=SoftDrinkSerializer(data=request.GET)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
def softDrinks_Detail(request,id):
    try:
        drink=soft_drink.objects.get(pk=id)
    except soft_drink.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer=SoftDrinkSerializer(drink)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer=SoftDrinkSerializer(drink,data=request.GET)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        drink.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



@api_view(['GET', 'POST'])
def AlcoholDrink(request):
    try:
        my_alcohol = alcohol.objects.all()
    except alcohol.DoesNotExist:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'GET':
        serialized_alcohol=AlcoholSerializer(my_alcohol, many=True)
        return Response(serialized_alcohol.data)
    elif request.method == 'POST':
        serializer =AlcoholSerializer(data=request.GET)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET','PUT','DELETE'])
def AlcoholDrink_Detail(request,id):
    try:
        get_alcohol=alcohol.objects.get(pk=id)
    except alcohol.DoesNotExist:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    if request.method =='GET':
        serializer=AlcoholSerializer(get_alcohol)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method =='PUT':
        serializer=AlcoholSerializer(get_alcohol,data=request.GET)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method =='DELETE':
        get_alcohol.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
          

@api_view(['GET', 'POST'])
def sodaDrink(request):
    try:
        sodas=soda.objects.all()
    except soda.DoesNotExist:
        return Response(status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'GET':
        serialized_sodas=SodaSerializer(sodas, many=True)
        return Response(serialized_sodas.data)
    elif request.method == 'POST':
        serializer=SodaSerializer(data=request.GET)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET','PUT','DELETE'])
def sodaDrink_Detail(request,id):
    try:
        get_soda = soda.objects.get(pk=id)
    except soda.DoesNotExist:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'GET':
        serializer=SodaSerializer(get_soda)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        serializer=SodaSerializer(get_soda,data=request.GET)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        get_soda.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)