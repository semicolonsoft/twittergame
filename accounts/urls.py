from django.urls import path
from .views import *

urlpatterns = [
    path('signup', register.as_view()),
    path('is_login', is_login.as_view()),
    path('follow', follow.as_view()),


]
