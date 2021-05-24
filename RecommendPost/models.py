from django.db import models

class seenPostClass(models.Model):
    UserName = models.CharField(max_length=40,unique=False,default="None")
    PostId = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True, editable=False)

    def __str__(self):
        return self.UserName
