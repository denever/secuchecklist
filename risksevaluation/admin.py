from risksevaluation.models import RisksEvaluationDocument, RiskFactorEvaluation

from django.contrib import admin

class RisksEvaluationDocumentAdmin(admin.ModelAdmin):
    list_display = ('record_date', 'revision_description', 'record_by')
    list_filter = ['record_date']
    search_fields = ['revision_description']
    date_hierarchy = 'record_date'

admin.site.register(RisksEvaluationDocument, RisksEvaluationDocumentAdmin)
admin.site.register(RiskFactorEvaluation)
