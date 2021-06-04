from django.db import models

class archivePostClass(models.Model):
    UserName = models.CharField(max_length=40,unique=False,default="None")
    PostId = models.IntegerField()
    Collection = models.CharField(max_length=40,unique=False,default="Main")