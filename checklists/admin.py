from checklists.models import CheckList, RiskFactorEvaluation

from django.contrib import admin

# class CheckListAdmin(admin.ModelAdmin):
#     list_display = ('description',)
#     list_filter = ['description']
#     search_fields = ['description', 'question', 'measure', 'link']
#     date_hierarchy = 'record_date'


admin.site.register(CheckList)
admin.site.register(RiskFactorEvaluation)
