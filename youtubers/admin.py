from django.contrib import admin
from .models import Youtuber
from django.utils.html import format_html


# Register your models here.
class YtAdmin(admin.ModelAdmin):
    def myphoto(self, object):
        return format_html(f'<img src={object.photo.url} width="40" />') 

    list_display = ('id','myphoto', 'name', 'subs_count', 'is_featured','price')
    search_fields = ('name', 'camera_type')
    list_filter = ('city', 'camera_type')
    list_display_links = ('id', 'name')
    list_editable = ('is_featured','price')



admin.site.register(Youtuber, YtAdmin)


