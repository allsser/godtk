from django.contrib import admin
from .models import Godtk
from .models import Hashtag

class GodtkAdmin(admin.ModelAdmin):
  list_display = ('event_title','company_name','start_date','end_date','tag', 'content', 'event_url', 'img_path')

class HashtagAdmin(admin.ModelAdmin):
    list_display = ('tag',)

admin.site.register(Godtk, GodtkAdmin)
admin.site.register(Hashtag, HashtagAdmin)