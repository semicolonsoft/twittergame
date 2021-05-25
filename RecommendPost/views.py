from Post.models import postClass
from django.shortcuts import render
from rest_framework import viewsets
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from django.http import HttpResponse
from rest_framework.response import Response
from datetime import datetime

from .serializers import seenPostClassSerializer
from .models import seenPostClass
from accounts.serializers import UserSerializer

from Post.serializers import postClassSerializer
from Post.models import postClass

class seenPostClassViewSet(viewsets.ModelViewSet):
    queryset = seenPostClass.objects.all()
    serializer_class = seenPostClassSerializer


@csrf_exempt
@api_view(('GET','DELETE','POST'))
def RecomPost(request):

    # if(request.user.is_anonymous):
    #     return HttpResponse("you have to login first!",status=403)

    if request.method == 'POST':
        mainPostId = request.POST['PostId']
        if(seenPostClass.objects.filter(PostId=mainPostId).filter(UserName = request.user).count() != 0):
            return HttpResponse("You seen this photo before!",status=403)
        Obj = seenPostClass(PostId = mainPostId,UserName = request.user)
        Obj.save()
        return HttpResponse("POST was successful!",status=200)

    elif request.method == 'GET':
        mainPostId = request.POST["PostId"]
        if(seenPostClass.objects.filter(PostId=mainPostId).count() != 0):
            snippets = seenPostClass.objects.filter(UserName = request.user)
            serializer = seenPostClassSerializer(snippets, many=True)
            return Response(serializer.data)
        elif(True):
            return HttpResponse("Does not exist",status=400)

@csrf_exempt
@api_view(('GET','DELETE','POST'))
def SendRecomPost(request):

    now = datetime.now()
    count = seenPostClass.objects.all().count()
    hold = seenPostClass.objects.all()
    for x in range (count):
        Date = hold[x].date
        if ((int(now.strftime("%j")) >= int(Date.strftime("%j")) + 14) &
         (int(now.strftime("%Y")) == int(Date.strftime("%Y")))): 
            obj = hold[x]
            obj.beDelete = 1
            obj.save()
    for x in range(count):
        seenPostClass.objects.filter(beDelete = 1).delete()
            

    A = 7 #followers RecommendPost Numbers
    B = 2 #most likes post Numbers
    C = 2 #followers of followers RecommendPost Numbers

    if request.method == 'GET':
        userCount = request.user.followers.all().count()
        followers = request.user.followers.all()
        arr = []
        array = []
        for y in range(userCount):
            try:
                hold = followers[y]
                count = postClass.objects.filter(UserName = hold).count()
                for x in range(count) :     
                    if seenPostClass.objects.filter(PostId = postClass.objects.filter(UserName = hold)[x].postId,UserName = request.user).count() == 0:
                        holdDate = postClass.objects.all()[x].date
                        if((int(now.strftime("%j")) <= int(holdDate.strftime("%j")) + 14) &
                         (int(now.strftime("%Y")) == int(holdDate.strftime("%Y")))):
                            arr.insert(0,[postClass.objects.filter(UserName = hold)[x].date,postClass.objects.filter(UserName = hold)[x].postId])
                    elif(True):
                        count += 1
            except:
                print("handel 1")
        arr.sort()
        print(arr)
        if len(arr) < A :
            B += A - len(arr)
            A= len(arr)
        for x in range(len(arr) - A , len(arr)):
            snippets = postClass.objects.filter(postId=arr[x][1])
            serializer = postClassSerializer(snippets, many=True)
            array.insert(0,serializer.data)

        arr.clear()
        holdCount = postClass.objects.all().count()
        for x in range(holdCount):
            try:
                hold = postClass.objects.all()[x].like
                if seenPostClass.objects.filter(PostId = postClass.objects.all()[x].postId,UserName = request.user).count() == 0:
                    holdDate = postClass.objects.all()[x].date
                    if((int(now.strftime("%j")) <= int(holdDate.strftime("%j")) + 14) &
                     (int(now.strftime("%Y")) == int(holdDate.strftime("%Y")))):
                        arr.insert(0,[hold,postClass.objects.all()[x].postId])
                elif(True):
                    holdCount += 1
            except:   
                print("handel 2")

        arr.sort()
        if len(arr) < B :
            C += B - len(arr)
            B = len(arr)
        for x in range(len(arr) - B , len(arr)):
            snippets = postClass.objects.filter(postId=arr[x][1])
            serializer = postClassSerializer(snippets, many=True)
            array.insert(0,serializer.data)

        arr.clear()
        followersF = []
        for x in range(userCount):
            followersF.insert(0,followers[x].followers.all())
        for x in range(len(followersF)):
            for y in range(len(followersF[x])):
                hold = followersF[x][y]
                count = postClass.objects.filter(UserName = hold).count()
                for z in range(count) : 
                    try:
                        if seenPostClass.objects.filter(PostId = postClass.objects.filter(UserName = hold)[z].postId,UserName = request.user).count() == 0:
                            holdDate = postClass.objects.all()[z].date
                            if((int(now.strftime("%j")) <= int(holdDate.strftime("%j")) + 14) &
                             (int(now.strftime("%Y")) >= int(holdDate.strftime("%Y")))):
                                arr.insert(0,[postClass.objects.filter(UserName = hold)[z].date,postClass.objects.filter(UserName = hold)[z].postId])
                        elif(True):
                            count += 1
                    except:
                        print("handel 3")   
        arr.sort()
        if len(arr) < C :
            C = len(arr)
        for x in range(len(arr) - C , len(arr)):
            snippets = postClass.objects.filter(postId=arr[x][1])
            serializer = postClassSerializer(snippets, many=True)
            array.insert(0,serializer.data)


        return Response(array)  
    return HttpResponse(status=200)
