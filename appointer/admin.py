
from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import Event, Signup

class EventAdmin(ModelAdmin):
    fieldsets = [
        (None, {"fields": ["name"]}),
        ("Date information", {"fields": ["start_timestamp", "end_timestamp"]}),
    ]
    list_display = ["name", "start_timestamp", "end_timestamp"]
    search_fields = ["name"]

admin.site.register(Event, EventAdmin)
admin.site.register(Signup)