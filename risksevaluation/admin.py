from risksevaluation.models import RisksEvaluationDocument, RiskFactorEvaluation

from django.contrib import admin
import reversion

class RisksEvaluationDocumentAdmin(reversion.VersionAdmin):
    list_display = ('title',)
    list_filter = ['title']
    search_fields = ['title']
    date_hierarchy = 'record_date'

admin.site.register(RisksEvaluationDocument, RisksEvaluationDocumentAdmin)
admin.site.register(RiskFactorEvaluation)
