from django.contrib import admin
from unfold.admin import ModelAdmin, TabularInline
from .models import Event, Foundation
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from unfold.contrib.import_export.forms import ExportForm, ImportForm


class EventInline(TabularInline):
    model = Event
    extra = 0

class FoundationResource(resources.ModelResource):
    class Meta:
        model = Foundation
        import_id_fields = ("name",)
        fields = (
            "name", "contact", "email", "phone", "website",
            "social_links", "sector", "location", "description",
        )
        export_order = fields

@admin.register(Foundation)
class FoundationAdmin(ModelAdmin, ImportExportModelAdmin):
    resource_classes = [FoundationResource]
    import_form_class = ImportForm
    export_form_class = ExportForm
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