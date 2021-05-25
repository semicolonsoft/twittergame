from rest_framework import serializers
from . models import seenPostClass

class seenPostClassSerializer(serializers.HyperlinkedModelSerializer):
    class Meta :
        model = seenPostClass
        fields = ('UserName' ,'PostId' , 'date' , 'beDelete')

