from django.urls import path
from .views import *

urlpatterns = [
    path('Posts', Posts.as_view()),
    path('Replays', Replays.as_view()),
    path('Like', Like.as_view()),
]
