from rest_framework import serializers

from . models import archivePostClass

class archivePostClassSerializer(serializers.HyperlinkedModelSerializer):
    class Meta :
        model = archivePostClass
        fields = ('UserName', 'PostId' , 'Collection')

