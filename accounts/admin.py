from django.contrib import admin
from .models import User


# Register your models here.
# class Admin(admin.ModelAdmin):
#     list_display=('username','id')
#     search_fields=('username','id')
#     ordering=('id','username')
#     list_filter=('id','username')

admin.site.register(User)