from django.shortcuts import render
from rest_framework import viewsets
from django.http import JsonResponse
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib import auth
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token

from .serializers import gameRecClassSerializer
from .models import gameRecClass

class gameRecClassViewSet(viewsets.ModelViewSet):
    queryset = gameRecClass.objects.all().order_by('date')
    serializer_class = gameRecClassSerializer

@csrf_exempt
@api_view(('GET','DELETE'))
def GameRec(request):
    if request.method == 'GET':
        user = request.GET["UserName"]
        if(gameRecClass.objects.filter(UserName=user).count() != 0):
            snippets = gameRecClass.objects.filter(UserName=user)
            serializer = gameRecClassSerializer(snippets, many=True)
            return Response(serializer.data)
        elif(True):
            return HttpResponse("Does not exist",status=400)
    
    elif request.method == 'DELETE':
        user = request.GET['UserName']
        Game = request.GET['GameName']

        if(gameRecClass.objects.filter(UserName = user).filter(GameName = Game).count() == 0):
            return HttpResponse("Does not exist",status=400)
        
        gameRecClass.objects.filter(UserName = user).filter(GameName = Game).delete()
        return HttpResponse("DELETE was successful!",status=200)
