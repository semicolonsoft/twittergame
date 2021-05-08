from django.db import models
from django.core.exceptions import ValidationError

class postClass(models.Model) :

    def file_size(value):
        limit = 2 * 1024 * 1024
        if value.size > limit:
            raise ValidationError('File too large. Size should not exceed 2 MiB.')

    UserName = models.CharField(max_length=40,unique=False)
    message = models.CharField(max_length = 200,null = True,blank = True)
    postId = models.AutoField(primary_key=True)
    date = models.DateTimeField(auto_now_add=True, editable=False)
    image = models.ImageField('image',blank = True,null=True, validators=[file_size])

    def __str__(self) :
        return self.message

class replayClass(models.Model):
    mainPost = models.IntegerField()
    subPost = models.IntegerField()

    def __str__(self):
        return self.mainPost

class likesClass(models.Model):
    PostId = models.IntegerField()
    UserName = models.CharField(max_length=40,unique=False)

    def __str__(self):
        return self.PostId

