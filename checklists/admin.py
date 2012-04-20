from checklists.models import Checklist, RiskFactorEvaluation

from django.contrib import admin
import reversion

class ChecklistAdmin(reversion.VersionAdmin):
    # list_display = ('description',)
    # list_filter = ['description']
    # search_fields = ['description', 'question', 'measure', 'link']
    # date_hierarchy = 'record_date'
    pass

admin.site.register(Checklist, ChecklistAdmin)
admin.site.register(RiskFactorEvaluation)
