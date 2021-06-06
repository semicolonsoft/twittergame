from django.shortcuts import render
from rest_framework import viewsets
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.decorators import api_view


from .serializers import archivePostClassSerializer
from .models import archivePostClass

class likesClassViewSet(viewsets.ModelViewSet):
    queryset = archivePostClass.objects.all()
    serializer_class = archivePostClassSerializer


@csrf_exempt
@api_view(('GET','DELETE','PATCH','POST'))
def ArchivePost(request):

    if(request.user.is_anonymous):
        return HttpResponse("you have to login first!",status=403)

    if request.method == 'POST':
        postId = request.POST["PostId"]
        collection = request.POST["Collection"]
        
        if(archivePostClass.objects.filter(UserName=request.user).filter(PostId=postId).filter(Collection=collection).count() == 0):
            if (collection == ""):
                collection = "Main"
            Obj = archivePostClass(PostId = postId,UserName=request.user,Collection = collection)
            Obj.save()
            return HttpResponse("POST was successful!",status=200)
        elif(True):
            return HttpResponse("You cant Save a post,Twice!",status=400)

    elif request.method == 'GET':
        option = request.GET["Option"]
        if(option == "1"):
            if(archivePostClass.objects.filter(UserName=request.user).count() != 0):

                snippets = archivePostClass.objects.filter(UserName=request.user).reverse()
                serializer = archivePostClassSerializer(snippets, many=True)
                return Response(serializer.data)
            return HttpResponse("Does not exist",status=400)

        elif(option == "2"):
            collection = request.POST["Collection"]
            if(archivePostClass.objects.filter(UserName=request.user).filter(Collection = collection).count() != 0):
                snippets = archivePostClass.objects.filter(UserName=request.user).filter(Collection = collection).reverse()
                serializer = archivePostClassSerializer(snippets, many=True)
                return Response(serializer.data)
            return HttpResponse("Does not exist",status=400)

    elif request.method == 'DELETE':
        option = request.POST["Option"]
        if(option == "1"):
            postId = request.POST['PostId']
            if(archivePostClass.objects.filter(PostId = postId).count() != 0):
                archivePostClass.objects.filter(PostId = postId).delete()
                return HttpResponse("Delete was successful",status=200)
            return HttpResponse("Post does not exist",status=400)
        
        if(option == "2"):
            collection = request.POST["Collection"]
            if(archivePostClass.objects.filter(Collection = collection).count() != 0):
                archivePostClass.objects.filter(Collection = collection).delete()
                return HttpResponse("Delete was successful",status=200)
            return HttpResponse("Collection does not exist",status=400)
    


