from django.urls import path
from .views import *

urlpatterns = [
    path('seenPost', RecomPost),
    path('SendRecomPost', SendRecomPost),
    path('SendRecomPostBot', SendRecomPostBot),
]
