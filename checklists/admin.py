from checklists.models import CheckList, RiskFactorEvaluation

from django.contrib import admin
import reversion

class CheckListAdmin(reversion.VersionAdmin):
    # list_display = ('description',)
    # list_filter = ['description']
    # search_fields = ['description', 'question', 'measure', 'link']
    # date_hierarchy = 'record_date'
    pass

admin.site.register(CheckList, CheckListAdmin)
admin.site.register(RiskFactorEvaluation)
