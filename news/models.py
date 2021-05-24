from django.db import models
from django.contrib import admin


class News(models.Model):
    title=models.CharField(max_length=100)
    body=models.TextField(max_length=2000)
    image=models.URLField()
    src_name=models.CharField(max_length=20)
    src_link=models.URLField()
    src_image=models.URLField()
    date=models.DateField()
    pump=models.IntegerField()
    dump=models.IntegerField()
    link_arzdg=models.URLField()
    post_id_arzdg=models.CharField(max_length=10)



    def __str__(self):
        return self.title

