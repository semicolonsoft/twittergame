from rest_framework import serializers

from .models import postClass
from .models import replayClass
from .models import likesClass

class postClassSerializer(serializers.HyperlinkedModelSerializer):
    class Meta :
        model = postClass
        fields = ('message', 'postId' , 'date' ,'UserName','image','like')

class replayClassSerializer(serializers.HyperlinkedModelSerializer):
    class Meta :
        model = replayClass
        fields = ('mainPost', 'subPost','UserName')


class likesClassSerializer(serializers.HyperlinkedModelSerializer):
    class Meta :
        model = likesClass
        fields = ('PostId', 'UserName')

