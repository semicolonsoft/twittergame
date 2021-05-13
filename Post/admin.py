from django.contrib import admin

from .models import postClass
from .models import replayClass
from .models import likesClass

admin.site.register(postClass)
admin.site.register(replayClass)
admin.site.register(likesClass)
