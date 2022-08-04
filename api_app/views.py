from django.shortcuts import render
from rest_framework.decorators import api_view
from .serializers import drinkserializer
from django.http import JsonResponse
from .models import drink

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.


@api_view(['GET','POST'])
def drink_list(request):
    if request.method=="GET":
        all_drinks=drink.objects.all()
        s=drinkserializer(all_drinks,many=True)
        return JsonResponse({"drinks":s.data})
    if request.method=="POST":
        new=drinkserializer(data=request.data)
        if new.is_valid():
            new.save()
            return Response(new.data,status=status.HTTP_201_CREATED)

@api_view(['GET','PUT','DELETE'])
def drink_detail(request,id):
    try:
        single=drink.objects.get(pk=id)
    except drink.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method=='GET':
        object=drinkserializer(single)
        return Response(object.data)
    elif request.method=='PUT':
        updated_drink=drinkserializer(single,data=request.data)
        if updated_drink.is_valid():
            updated_drink.save()
            return Response(updated_drink.data,status=status.HTTP_200_OK)
        return Response(updated_drink.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method=="DELETE":
        single.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)

