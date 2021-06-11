from django.shortcuts import render
from rest_framework import viewsets
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.decorators import api_view
from PIL import Image


from .serializers import likesClassSerializer
from .models import likesClass

from .serializers import postClassSerializer
from .models import postClass

from .serializers import replayClassSerializer
from .models import replayClass



class likesClassViewSet(viewsets.ModelViewSet):
    queryset = likesClass.objects.all()
    serializer_class = likesClassSerializer

class postClassViewSet(viewsets.ModelViewSet):
    queryset = postClass.objects.all()
    serializer_class = postClassSerializer

class replayClassViewSet(viewsets.ModelViewSet):
    queryset = replayClass.objects.all()
    serializer_class = replayClassSerializer

@csrf_exempt
@api_view(('GET','DELETE','PATCH','POST'))
def Posts(request):

    if(request.user.is_anonymous):
        return HttpResponse("you have to login first!",status=403)

    if request.method == 'POST':
        messageTxt = request.POST["message"]
        if(True):
            try:
                imageFile = request.FILES["image"]
                if not imageFile == None:
                    try:
                        Image.open(imageFile)
                    except:
                        return HttpResponse("sorry, your image is invalid",status=400)
                    if(len(Image.open(imageFile).fp.read()) > 5000000):
                        return HttpResponse("File too large. Size should not exceed 5 MB.",status=403)
                    elif(len(Image.open(imageFile).fp.read()) < 10000):
                        return HttpResponse("The size should not be less than 10 KB",status=403)
                    Obj = postClass(message = messageTxt,UserName=request.user,image = imageFile,like = 0)
                    Obj.save()

            except:
                Obj = postClass(message = messageTxt,UserName=request.user,like = 0)
                Obj.save()
        return HttpResponse("POST was successful!",status=200)

    elif request.method == 'GET':
        User = request.GET["UserName"]
        if(postClass.objects.filter(UserName=User).count() != 0):

            snippets = postClass.objects.filter(UserName=User).order_by('date').reverse()
            serializer = postClassSerializer(snippets, many=True)
            return Response(serializer.data)

        return HttpResponse("Does not exist",status=400)
    
    elif request.method == 'DELETE':
        chatId = request.POST['postId']
        if(postClass.objects.filter(postId = chatId).count() != 0):
            if(postClass.objects.filter(postId = chatId).filter(UserName = request.user).count() == 0):
                return HttpResponse("You can only delete your own posts!",status=403)
            postClass.objects.filter(postId = chatId).delete()
            return HttpResponse("DELETE was successful!",status=200)
        return HttpResponse("Does not exist",status=400)


    elif request.method == 'PATCH':
        chatId = request.POST['postId']
        if(postClass.objects.filter(postId = chatId).count() != 0):
            if(postClass.objects.filter(postId = chatId).filter(UserName = request.user).count() == 0):
                return HttpResponse("You can only edit your own posts!",status=403)
            hold = postClass.objects.get(postId = chatId)
            hold.message = request.POST['newMessage']
            hold.save()
            return HttpResponse("EDIT was successful!",status=200)
        return HttpResponse("Does not exist",status=400)

@csrf_exempt
@api_view(('GET','DELETE','POST'))
def Replays(request):

    if(request.user.is_anonymous):
        return HttpResponse("you have to login first!",status=403)

    if request.method == 'POST':
        mainPostId = request.POST['mainPost']
        messageTxt = request.POST["message"]
        Obj = postClass(message = messageTxt,UserName=request.user,like = 0)
        Obj.save()
        
        subPostId = Obj.postId
        if(postClass.objects.filter(postId=mainPostId).count() == 0):
            if(postClass.objects.filter(postId=subPostId).count() == 0):
                return HttpResponse("mainPostId & subPostId not exist",status=400)
            elif(True):
                return HttpResponse("mainPostId not exist",status=400)
        elif(postClass.objects.filter(postId=subPostId).count() == 0):
            return HttpResponse("subPostId not exist",status=400)

        Obj = replayClass(mainPost = mainPostId,subPost = subPostId,UserName=request.user,message = messageTxt)
        Obj.save()
        return HttpResponse("POST was successful!",status=200)

    elif request.method == 'GET':
        mainPostId = request.GET["mainPost"]
        if(replayClass.objects.filter(mainPost=mainPostId).count() != 0):
            snippets = replayClass.objects.filter(mainPost=mainPostId)
            serializer = replayClassSerializer(snippets, many=True)
            return Response(serializer.data)
        elif(True):
            return HttpResponse("Does not exist",status=400)
    
    elif request.method == 'DELETE':
        mainPostId = request.POST['mainPost']
        subPostId = request.POST['subPost']
        if(replayClass.objects.filter(mainPost = mainPostId).filter(subPost = subPostId).count() != 0):
            if(replayClass.objects.filter(mainPost = mainPostId).filter(subPost = subPostId)
                .filter(UserName=request.user).count() == 0):
                return HttpResponse("You can only delete your own likes!",status=401)
            replayClass.objects.filter(mainPost = mainPostId).filter(subPost = subPostId).delete()
            return HttpResponse("DELETE was successful!",status=200)
        return HttpResponse("Does not exist",status=400)

@csrf_exempt
@api_view(('GET','DELETE','POST'))
def Like(request):

    if(request.user.is_anonymous):
        return HttpResponse("you have to login first!",status=403)

    if request.method == 'POST':
        mainPostId = request.POST['PostId']
        try :
            if(likesClass.objects.filter(PostId=mainPostId).filter(UserName = request.user).count() != 0):
                likesClass.objects.filter(PostId = mainPostId).filter(UserName = request.user).delete()
                hold = postClass.objects.get(postId = mainPostId)
                hold.like -= 1
                hold.save()
                return HttpResponse("DELETE was successful!",status=200)
            
            Obj = likesClass(PostId = mainPostId,UserName = request.user)
            Obj.save()
            hold = postClass.objects.get(postId = mainPostId)
            hold.like += 1
            hold.save()
            postClass.objects.filter(postId = mainPostId).like = 1
            return HttpResponse("POST was successful!",status=200)
        except :
            return HttpResponse("This PostId isn't exist!",status=400)

    elif request.method == 'GET':
        mainPostId = request.GET["PostId"]
        if(likesClass.objects.filter(PostId=mainPostId).count() != 0):
            snippets = likesClass.objects.filter(PostId=mainPostId)
            serializer = likesClassSerializer(snippets, many=True)
            return Response(serializer.data)
        elif(True):
            return HttpResponse([],status=204)

    
    elif request.method == 'DELETE':
        mainPostId = request.POST['PostId']
        if(likesClass.objects.filter(PostId = mainPostId).count() != 0):
            if(likesClass.objects.filter(PostId = mainPostId).filter(UserName = request.user).count() == 0):
                return HttpResponse("You can only delete your own likes!",status=401)
            likesClass.objects.filter(PostId = mainPostId).filter(UserName = request.user).delete()
            hold = postClass.objects.get(postId = mainPostId)
            hold.like -= 1
            hold.save()
            return HttpResponse("DELETE was successful!",status=200)
        return HttpResponse("Does not exist",status=400)

@csrf_exempt
@api_view(('GET','POST'))
def ExtLike(request):

    if(request.user.is_anonymous):
        return HttpResponse("you have to login first!",status=403)

    if request.method == 'GET':
        mainPostId = request.GET["PostId"]
        if(likesClass.objects.filter(PostId=mainPostId).filter(UserName = request.user).count() != 0):
            return HttpResponse(True,status=200)
        return HttpResponse(False,status=200)

    


             