from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from . import settings

from rest_framework import routers
from Post import views
from GameBar.views import gameRecClassViewSet
from Post.views import Posts
from Post.views import Replays
from Post.views import Like
from GameBar.views import GameRec

router = routers.DefaultRouter()
router.register(r'postClass', views.postClassViewSet)
router.register(r'replayClass', views.replayClassViewSet)
router.register(r'likesClass', views.likesClassViewSet)
router.register(r'GameRecClass', gameRecClassViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('Posts',Posts),
    path('Replays',Replays),
    path('Like',Like),
    path('GameRec',GameRec),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    path('admin/', admin.site.urls),
    path('account/', include('accounts.urls')),
    path('Post/', include('Post.urls')),
    path('RecommendPost/', include('RecommendPost.urls')),
    path('GameBar/', include('GameBar.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

