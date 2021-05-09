from django.shortcuts import render
from accounts.models import User
from django.http import JsonResponse
from django.contrib import auth
from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from django.forms.models import model_to_dict
from django.core import serializers
from .serializers import UserSerializer
from django.views.decorators.csrf import csrf_exempt

class follow(APIView):
    permission_classes = [IsAuthenticated]
    @csrf_exempt
    def post(self, request):
        user = User.objects.filter(username=request.POST["username"])
        if not user:
            return Response({'status':'fail!', 'message':'invalide username'})
        if request.user == user:
            return Response({'status':'fail!', 'message':'self follwoing'})
        if  user[0] in request.user.following.all():
            request.user.following.remove(user[0])

        else:
            request.user.following.add(user[0])
        return Response({'status':'success'})


class register(APIView):
    @csrf_exempt
    def post(self, request):
        username_=request.POST["username"]
        email_=request.POST["email"]
        password_=request.POST["password"]
        password2_=request.POST["confirmpassword"]

        if password2_!=password_:
            return JsonResponse({"status":"fail!","message":"password not equal"})

        same=User.objects.filter(username=username_)

        if  same:
            return JsonResponse({"status":"fail!","message":"username repeated!"})

        new_user=User(username=username_,email=email_)
        new_user.set_password(password_)

        try:
            new_user.image = request.FILES['image']

            new_user.bio = request.POST['bio']

        except:
            pass


        new_user.save()
        token = Token.objects.create(user=new_user)
        auth.login(request, new_user)
        return JsonResponse({"status":"True","message":f"welcome {username_} dear!", 'token':f'Token {token.key}'})

class login(APIView):
    @csrf_exempt
    def post(self,request):
        password_=request.POST["password"]
        #if user enter email
        if '@' in request.POST['usernameormail']:
            myuser = User.objects.filter(email=request.POST['usernameormail'])[0]
        #if user enter username
        else:
            myuser = User.objects.filter(username=request.POST['usernameormail'])[0]



        if  myuser.check_password(password_) :
            auth.login(request, myuser)
            token = Token.objects.get(user=myuser)
            return JsonResponse({'status':'success', 'token':f'Token {token.key}'})

        elif not myuser:
            return JsonResponse({'status':'fail' ,'message':'user not found'})
        else:

            return JsonResponse({'status':'fail','message':'wrong password'})


class update_profile(APIView):
    permission_classes=[IsAuthenticated]
    @csrf_exempt

    def post(self,req):
        myuser=User.objects.filter(username=req.user.username)[0]
        print(myuser.email)
        try:
            myuser.bio=req.POST["bio"]
            myuser.save()
        except:
            pass
        try:
            myuser.image=req.FILES["image"]

        except:
            return Response({'status':'fail','message':'not change'})

        return Response({'status':'true','message':'profile updated!'})

class is_login(APIView):
    # permission_classes = [IsAuthenticated]
    @csrf_exempt

    def get(self, req):
        if req.user.is_authenticated:
            try:
                return Response({'status':'true','id':req.user.username,'bio':req.user.bio,'following_num':req.user.following.count(),'follower_num':req.user.followers.count(),'image':req.user.image.url})

            except:
                return Response({'status':'true','id':req.user.username,'following_num':req.user.following.count(),'follower_num':req.user.followers.count()})
        else:
            return Response({"status":"fail"})


class getprofile(APIView):
    @csrf_exempt

    def get(self,req):
        return Response({'id':req.user.username,'bio':req.user.bio,'following_num':req.user.following.count(),'follower_num':req.user.followers.count(),'image':req.user.image.url})

class getimage(APIView):
    @csrf_exempt
    def get(self,req):
        return Response({'image':req.user.image.url})


class getfollowers(APIView):
    @csrf_exempt
    def get(self,req):
        followers=req.user.followers.all()

        b=UserSerializer(followers,many=True)
        return Response(b.data)



class getfollowings(APIView):
    @csrf_exempt

    def get(self,req):
        followings=req.user.following.all()
        b=UserSerializer(followings,many=True)
        return Response(b.data)



class getsuggested(APIView):
    @csrf_exempt

    def post(self,req):
        a=User.objects.filter(username=req.POST["username"])
        # a=req.user.suggested()
        b=UserSerializer(a,many=True)
        return Response(b.data)

class get_user_id(APIView):
    @csrf_exempt

    def get(self,req):
        a=req.POST['id']
        n=User.objects.count()

        if int(a)>n:
            return Response({'status':'fail'})
        else:

            b=User.objects.get(id=a)
        # # print(b)
        # c=UserSerializer(b,many=True)
        # print()
            return Response({"username":b.username,"email":b.email,"image":b.image.url})


# ffclass search(APIView):
#     @csrf_exempt
#     def(self,req):




def verify_code(req):
    #if user enter email
    if '@' in req.POST['username']:
        user = User.objects.filter(email=req.POST['username'])
    #if user enter username
    else:
        user = User.objects.filter(username=req.POST['username'])
    if not user:
        return JsonResponse({'status':'failed', 'error':'invalid username'})
    #check verification code and its passed time
    if str(user[0].verification_code) == req.POST.get('verification_code'): #and (timezone.now()-user[0].verification_code_time).total_seconds()<120:
        user[0].verified_email = True
        user[0].save()
        auth.login(req, user[0])
        return JsonResponse({'status':'success', 'token':user[0].session_id})
    return JsonResponse({'status':'failed', 'error':'invalid code'})
def resend_verification_code(req):
    user = User.objects.filter(username=req.POST['username'])
    if not user:
        return JsonResponse({'status':'failed', 'error':'invalid username'})
    user[0].verification_code = random.randint(10000, 99999)
    user[0].verification_code_time = timezone.now()
    user[0].save()
    send_mail(
    subject='A Cool Name account verification',
    message=f'your code to verify email : {user[0].verification_code}',
    from_email=settings.EMAIL_HOST_USER,
    recipient_list=[user[0].email],
    )
    return JsonResponse({'status':'success'})

def forget_password(request):
    user = User.objects.filter(email=request.POST('email'))
    if not user:
        return JsonResponse({'status':'failed', 'error':'invalid email'})
    user = user[0]
    new_password = random_string_generator()
    user.set_password(new_password)
    send_mail(
        subject='A Cool Name forget password',
        message=f'your new password is :  {new_password}   ""Please set new password after login!""',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[user.email],
    )
    user.save()
    return JsonResponse({'status':'success'})

    # def give_follow()