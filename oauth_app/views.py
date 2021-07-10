import mimetypes
import os
import requests

from accounts.models import User
from allauth.socialaccount.models import SocialAccount
from django.http import HttpResponse
from django.http.response import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from django.contrib import auth
from rest_framework.authtoken.models import Token


@csrf_exempt
@api_view(('GET','DELETE','PATCH','POST'))
def GoogleLogIn(request):
    if request.method == 'GET':
        counter = SocialAccount.objects.all().count() 
        email = SocialAccount.objects.all()[counter-1].extra_data['email']
        given_name = SocialAccount.objects.all()[counter-1].extra_data['given_name'].lower()
        try:
            userHold = User.objects.filter(email=email).get()
            userHold.GoogleAcc = True
            try:
                Token.objects.create(user=userHold)
                return HttpResponse(True,status=200)
            except:
                return HttpResponse(False,status=200)
        except :
            User.objects.filter(email=email).filter(GoogleAcc = True).delete()
            auth.login(request, userHold)

def download_file(request):
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    filename = 'test.txt'
    filepath = BASE_DIR + '/' + filename
    path = open(filepath, 'r')
    mime_type, _ = mimetypes.guess_type(filepath)
    response = HttpResponse(path, content_type=mime_type)
    response['Content-Disposition'] = "attachment; filename=%s" % filename
    return response