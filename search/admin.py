from django.contrib import admin

from .models import data

class DataAdmin(admin.ModelAdmin):
    list_display = ("chapter", "chapter_name", "section", "section_name", "description")

admin.site.register(data, DataAdmin)
