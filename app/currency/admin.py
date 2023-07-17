from django.contrib import admin
from rangefilter.filters import DateRangeFilter
from import_export.admin import ImportExportModelAdmin

from currency.models import Rate


@admin.register(Rate)
class RateAdmin(ImportExportModelAdmin):
    list_display = (
        'id',
        'buy',
        'sell',
        'currency',
        'source',
        'created'
    )
    list_filter = (
        'currency',
        ('created', DateRangeFilter)
    )
    search_fields = (
        'buy',
        'sell'
    )
    readonly_fields = (
        'buy',
        'sell'
    )

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False
