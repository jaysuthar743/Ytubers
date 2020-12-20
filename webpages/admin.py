from django.contrib import admin
from .models import Slider, Team
from django.utils.html import format_html

# add more columns of model
class TeamAdmin(admin.ModelAdmin):
    
    # inlines(this methods are called 'inline')
    #  this method are already exist, u have to just ovveride

    def myphoto(self, object):
        return format_html(f'<img src="{object.photo.url}"  width="40" />')

    list_display = ('id' ,'myphoto', 'first_name', 'last_name', 'role', 'created_date')
    list_display_links = ('first_name', 'id', 'myphoto')
    search_fields = ('first_name','role')
    list_filter = ('role', ) #filter, 

class TeamSlider(admin.ModelAdmin):
    list_display = ('headline', 'subtitle')

# Register your models here.
admin.site.register(Slider, TeamSlider)
admin.site.register(Team, TeamAdmin)

