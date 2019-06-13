from django.contrib import admin
from . models import Bible


class BibleAdmin(admin.ModelAdmin):
    list_display = ['name', 'image', 'mp3']


admin.site.register(Bible, BibleAdmin)
