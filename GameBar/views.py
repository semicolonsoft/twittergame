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
@api_view(('GET','DELETE','POST'))
def GameRec(request):
    
    # if(request.user.is_anonymous):
    #     return HttpResponse("you have to login first!",status=403)

    if request.method == 'POST':
        Game = request.POST['GameName']
        rec = request.POST['Record']

        Obj = gameRecClass(GameName = Game,Record = rec,UserName=request.user)
        Obj.save()
        return HttpResponse("POST was successful!",status=200)

    elif request.method == 'GET':
        user = request.GET["UserName"]
        if(gameRecClass.objects.filter(UserName=user).count() != 0):
            snippets = gameRecClass.objects.filter(UserName=user)
            serializer = gameRecClassSerializer(snippets, many=True)
            return Response(serializer.data)
        elif(True):
            return HttpResponse("Does not exist",status=400)
    
    elif request.method == 'DELETE':
        Game = request.POST['GameName']
        rec = request.POST['Record']
        if(rec==""):
            if(gameRecClass.objects.filter(GameName = Game).count() != 0):
                if(gameRecClass.objects.filter(GameName = Game).filter(UserName = request.user).count() == 0):
                    return HttpResponse("You can only delete your own records!",status=403)
                gameRecClass.objects.filter(GameName = Game).delete()
                return HttpResponse("DELETE was successful!",status=200)
            return HttpResponse("Does not exist",status=400)
        elif(True):
            if(gameRecClass.objects.filter(GameName = Game).filter(Record = rec).count() != 0):
                if(gameRecClass.objects.filter(GameName = Game).filter(Record = rec).filter(UserName = request.user).count() == 0):
                    return HttpResponse("You can only delete your own records!",status=403)
                gameRecClass.objects.filter(GameName = Game).filter(Record = rec).delete()
                return HttpResponse("DELETE was successful!",status=200)
            return HttpResponse("Does not exist",status=400)
