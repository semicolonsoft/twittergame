from django.urls import path
from .views import *

urlpatterns = [
    path('signup', register.as_view()),
    path('login', login.as_view()),
    path('update_profile', update_profile.as_view()),
    path('is_login', is_login.as_view()),
    path('follow', follow.as_view()),
    path('getprofile', getprofile.as_view()),
    path('getimage', getimage.as_view()),
    path('getfollowers', getfollowers.as_view()),
    path('getfollowings', getfollowings.as_view()),
    path('getsuggested', getsuggested.as_view()),
    path('get_user_id', get_user_id.as_view()),
    path('verify_code', verify_code.as_view()),
    path('resend_verification_code', resend_verification_code.as_view()),
    path('forget_password', forget_password.as_view()),
    path('search', search.as_view()),
    path('logout', logout.as_view()),


]
