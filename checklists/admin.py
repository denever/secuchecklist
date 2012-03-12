from checklists.models import RiskFactor

from django.contrib import admin

class RiskFactorAdmin(admin.ModelAdmin):
    list_display = ('description',)
    list_filter = ['description']
    search_fields = ['description', 'question', 'measure', 'link']
    date_hierarchy = 'record_date'


admin.site.register(RiskFactor, RiskFactorAdmin)
