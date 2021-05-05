from django.db import models

class gameRecClass(models.Model):
    GameName = models.CharField(max_length=20,unique=False)
    UserName = models.CharField(max_length=40,unique=False)
    Reocrd = models.IntegerField(default=0)
    date = models.DateTimeField(auto_now_add=True, editable=False)

    def __str__(self) :
        return self.GameName