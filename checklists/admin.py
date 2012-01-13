from checklists.models import Checklist, Check
from checklists.models import BooleanCheckResult, MultipleCheckResult, PercentageCheckResult
from django.contrib import admin

admin.site.register(Checklist)
admin.site.register(Check)
admin.site.register(BooleanCheckResult)
admin.site.register(MultipleCheckResult)
admin.site.register(PercentageCheckResult)
