from django.shortcuts import render
from rest_framework import viewsets
from django.http import JsonResponse
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.authtoken.models import Token

from .serializers import likesClassSerializer
from .models import likesClass

from .serializers import postClassSerializer
from .models import postClass

from .serializers import replayClassSerializer
from .models import replayClass


class likesClassViewSet(viewsets.ModelViewSet):
    queryset = likesClass.objects.all().order_by('PostId')
    serializer_class = likesClassSerializer

class postClassViewSet(viewsets.ModelViewSet):
    queryset = postClass.objects.all().order_by('message')
    serializer_class = postClassSerializer

class replayClassViewSet(viewsets.ModelViewSet):
    queryset = replayClass.objects.all().order_by('mainPost')
    serializer_class = replayClassSerializer

@csrf_exempt
@api_view(('GET','DELETE','PATCH'))
def Posts(request):
    if request.method == 'GET':
        token = Token.objects.get(uesr=user[0])
        print(token)
        print("1")
        User = request.GET["UserName"]
        if(postClass.objects.filter(UserName=User).count() != 0):
            snippets = postClass.objects.filter(UserName=User)
            serializer = postClassSerializer(snippets, many=True)
            return Response(serializer.data)

        return HttpResponse("Does not exist",status=400)
    
    elif request.method == 'DELETE':
        chatId = request.GET['postId']

        if(postClass.objects.filter(postId = chatId).count() == 0):
            return HttpResponse("Does not exist",status=400)

        elif(True):
            postClass.objects.filter(postId = chatId).delete()
            return HttpResponse("DELETE was successful!",status=200)
    
    elif request.method == 'PATCH':
        chatId = request.GET['postId']
        if(postClass.objects.filter(postId = chatId).count() == 0) :
            return HttpResponse("Does not exist",status=400)

        hold = postClass.objects.get(postId = chatId)
        hold.message = request.GET['newMessage']
        hold.save()
        return HttpResponse("EDIT was successful!",status=200)


@csrf_exempt
@api_view(('GET','DELETE'))
def Replays(request):
    if request.method == 'GET':
        mainPostId = request.GET["mainPost"]
        if(replayClass.objects.filter(mainPost=mainPostId).count() != 0):
            snippets = replayClass.objects.filter(mainPost=mainPostId)
            serializer = replayClassSerializer(snippets, many=True)
            return Response(serializer.data)
        elif(True):
            return HttpResponse("Does not exist",status=400)
    
    elif request.method == 'DELETE':
        mainPostId = request.GET['mainPost']
        subPostId = request.GET['subPost']

        if(replayClass.objects.filter(mainPost = mainPostId).filter(subPost = subPostId).count() == 0):
            return HttpResponse("Does not exist",status=400)
        
        replayClass.objects.filter(mainPost = mainPostId).filter(subPost = subPostId).delete()
        return HttpResponse("DELETE was successful!",status=200)


@csrf_exempt
@api_view(('GET','DELETE'))
def Like(request):
    if request.method == 'GET':
        mainPostId = request.GET["PostId"]
        if(likesClass.objects.filter(PostId=mainPostId).count() != 0):
            snippets = likesClass.objects.filter(PostId=mainPostId)
            serializer = likesClassSerializer(snippets, many=True)
            return Response(serializer.data)
        elif(True):
            return HttpResponse("Does not exist",status=400)

    
    elif request.method == 'DELETE':
        mainPostId = request.GET['PostId']
        user = request.GET['UserName']

        if(likesClass.objects.filter(PostId = mainPostId).filter(UserName = user).count() == 0):
            return HttpResponse("Does not exist",status=400)
        
        likesClass.objects.filter(PostId = mainPostId).filter(UserName = user).delete()
        return HttpResponse("DELETE was successful!",status=200)