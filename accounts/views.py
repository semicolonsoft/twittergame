from django.shortcuts import render
from accounts.models import User
from django.http import JsonResponse
from django.contrib import auth
from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token


class follow(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        user = User.objects.filter(username=request.POST["username"])
        if not user:
            return Response({'status':'fail!', 'message':'invalide username'})
        if request.user == user:
            return Response({'status':'fail!', 'message':'self follwoing'})
        request.user.following.add(user[0])
        return Response({'status':'success'})



class register(APIView):
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

        new_user=User(username=username_,password=password_,email=email_)
        new_user.image = request.FILES['image']
        new_user.save()
        token = Token.objects.create(user=new_user)
        auth.login(request, new_user)
        return JsonResponse({"status":"True","message":f"welcome {username_} dear!", 'token':f'Token {token.key}'})

###############333
class is_login(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, req):
        return Response({'status':'yes'})


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


def login(request):
    password_=request.POST["password"]
    #if user enter email
    if '@' in request.POST['usernameormail']:
        user = User.objects.filter(email=request.POST['usernameormail'])
    #if user enter username
    else:
        user = User.objects.filter(username=request.POST['usernameormail'])
    if user and password_==user[0].password:
        auth.login(request, user[0])
        token = Token.objects.get(uesr=user[0])
        return JsonResponse({'status':'success', 'token':f'Token {token.key}'})
        
    elif not user:
        return JsonResponse({'status':'fail' ,'message':'user not found'})
    else:

        return JsonResponse({'status':'fail','message':'wrong password'})





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