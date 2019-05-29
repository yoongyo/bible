from django.contrib import admin
from . models import Bible


class BibleAdmin(admin.ModelAdmin):
    list_display = ['name']


admin.site.register(Bible, BibleAdmin)
