"""twittergame URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from . import settings

from rest_framework import routers
from Post import views
from Post.views import Posts
from Post.views import Replays
from Post.views import Like

router = routers.DefaultRouter()
router.register(r'postClass', views.postClassViewSet)
router.register(r'replayClass', views.replayClassViewSet)
router.register(r'likesClass', views.likesClassViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('Posts',Posts),
    path('Replays',Replays),
    path('Like',Like),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    path('admin/', admin.site.urls),
    path('account/', include('accounts.urls')),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
