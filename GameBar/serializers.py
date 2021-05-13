from rest_framework import serializers
from .models import gameRecClass

class gameRecClassSerializer(serializers.HyperlinkedModelSerializer):
    class Meta :
        model = gameRecClass
        fields = ('GameName', 'UserName' ,'Record','date')
