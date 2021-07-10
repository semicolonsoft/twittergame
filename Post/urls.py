from django.urls import path
from .views import *

urlpatterns = [
    path('Posts', Posts),
    path('Replays', Replays),
    path('Like', Like),
    path('ExtLike', ExtLike),
]
from django.contrib import admin
from django.urls import include
from .views import test
