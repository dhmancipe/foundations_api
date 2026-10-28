from django.contrib import admin
from unfold.admin import ModelAdmin, TabularInline
from .models import Event, Foundation


class EventInline(TabularInline):
    model = Event
    extra = 0


@admin.register(Foundation)
class FoundationAdmin(ModelAdmin):
    list_display = ("name", "sector", "location", "website")
    list_filter = ("sector", "location")
    search_fields = ("name", "contact")
    inlines = [EventInline]


@admin.register(Event)
class EventAdmin(ModelAdmin):
    list_display = ("name", "foundation", "start_date", "end_date")
    list_filter = ("foundation", "start_date")
    search_fields = ("name", "description")
    date_hierarchy = "start_date"