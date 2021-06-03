from django.urls import path
from .views import *

urlpatterns = [
    path('Posts', Posts),
    path('Replays', Replays),
    path('Like', Like),
    path('ExtLike', ExtLike),
]
