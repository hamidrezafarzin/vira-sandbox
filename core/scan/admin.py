from django.contrib import admin

# Register your models here.

from .models import Scan

class ScanAdmin(admin.ModelAdmin):
    model = Scan
    search_fields = ("phone", "first_name", "last_name")
    list_filter = ("scan_part", "created_date", "updated_date")
    list_display = ("phone", "first_name", "last_name", "scan_part", "photo", "created_date")



admin.site.register(Scan, ScanAdmin)