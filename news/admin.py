  
from django.contrib import admin
from news.models import News
from django.db.models.functions import Lower
@admin.register(News)
class MyModelAdmin(admin.ModelAdmin):
    list_display = ('title','date','post_id_arzdg','src_name','dump','pump')
    search_fields = ['title']
    ordering = ['-post_id_arzdg']