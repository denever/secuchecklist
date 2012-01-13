from checklists.models import Checklist, Check
from checklists.models import BooleanCheckResult
from checklists.models import MultipleCheckResult
from checklists.models import PercentageCheckResult

from django.contrib import admin

class CheckInline(admin.StackedInline):
    model = Check
    extra = 10

class ChecklistAdmin(admin.ModelAdmin):
    list_display = ('title', 'date')
    list_filter = ['date']
    search_fields = ['title']
    date_hierarchy = 'date'
    
    fieldsets = [
        (None, {'fields': ['title']}),
        ('Date information', {'fields': ['date'], 'classes': ['collapse']}),
        ]
    inlines = [CheckInline]

admin.site.register(Checklist, ChecklistAdmin)
admin.site.register(Check)
admin.site.register(BooleanCheckResult)
admin.site.register(MultipleCheckResult)
admin.site.register(PercentageCheckResult)
