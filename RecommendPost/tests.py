from django.test import TestCase
from . models import seenPostClass
from Post.models import postClass
from . views import SendRecomPost
from django.http import HttpRequest

class seenPostClassTestCase(TestCase):
    def setUp(self):
        seenPostClass.objects.create(UserName = "Shayan" , PostId = 10)
        seenPostClass.objects.create(UserName = "Shayan" , PostId = 12)
        seenPostClass.objects.create(UserName = "Shayan2" , PostId = 11)
        seenPostClass.objects.create(UserName = "Shayan" , PostId = 7)
        seenPostClass.objects.create(UserName = "Shayan" , PostId = 7)

    def test_post_was_seen(self):
        postClass.objects.create(UserName = "reza" , message = "Shayan,Salam from reza" , like = 100)
        request = HttpRequest()
        request.method = 'POST'
        request.META['SERVER_NAME'] = 'http://127.0.0.1:8000/RecommendPost/seenPost'
        postId = postClass.objects.filter(UserName = "reza" , message = "Shayan,Salam from reza")[0].postId
        if(seenPostClass.objects.filter(UserName = "reza").filter(PostId = postId)):
            self.assertEqual(SendRecomPost(request), 'True')
        elif(True):
            self.assertEqual(SendRecomPost(request), 'False')
