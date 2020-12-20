from django.contrib import admin
from .models import Hireubers

# Register your models here.

class TeamHire(admin.ModelAdmin):
    list_display = ("first_name", "tuber_name")
    search_fields = ("tuber_name","first_name", "last_name")
    list_filter = ("tuber_name", )


admin.site.register(Hireubers, TeamHire)