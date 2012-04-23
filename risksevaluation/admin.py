from checklists.models import Checklist, RiskFactorEvaluation

from django.contrib import admin
import reversion

class ChecklistAdmin(reversion.VersionAdmin):
    list_display = ('title',)
    list_filter = ['title']
    search_fields = ['title']
    date_hierarchy = 'record_date'

admin.site.register(Checklist, ChecklistAdmin)
admin.site.register(RiskFactorEvaluation)
