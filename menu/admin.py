from django.contrib import admin
from .models import *


# admin.site.register(Event)

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('camera_id', 'time', 'link')
    list_filter = ('camera_id', 'time')


# @admin.register(FilterEvent)
# class FilterEventAdmin(admin.ModelAdmin):
#     list_filter = ('status', 'due_back')