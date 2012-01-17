from checklists.models import Checklist
from checklists.models import BooleanCheck
from checklists.models import SingleCheck, SingleChoice
from checklists.models import MultipleCheck, MultipleChoice
from checklists.models import NumericCheck

from django.contrib import admin

class BooleanCheckInline(admin.StackedInline):
    model = BooleanCheck
    extra = 1

class SingleCheckInline(admin.StackedInline):
    model = SingleCheck
    extra = 1
    
class MultipleCheckInline(admin.StackedInline):
    model = MultipleCheck
    extra = 1

class NumericCheckInline(admin.StackedInline):
    model = NumericCheck
    extra = 1

admin.site.register(BooleanCheck)

class SingleChoiceInline(admin.TabularInline):
    model = SingleChoice
    extra = 3

class SingleCheckAdmin(admin.ModelAdmin):
    list_display = ('descr', 'checklist')
    search_fields = ['descr']

    fieldsets = [
        (None, {'fields': ['checklist','descr']}),
        ]
    inlines = [SingleChoiceInline]

admin.site.register(SingleCheck, SingleCheckAdmin)


class MultipleChoiceInline(admin.TabularInline):
    model = MultipleChoice
    extra = 3

class MultipleCheckAdmin(admin.ModelAdmin):
    list_display = ('descr',)
    search_fields = ['descr']

    fieldsets = [
        (None, {'fields': ['checklist','descr']}),
        ]
    inlines = [MultipleChoiceInline]

admin.site.register(MultipleCheck, MultipleCheckAdmin)
admin.site.register(NumericCheck)

class ChecklistAdmin(admin.ModelAdmin):
    list_display = ('title', 'creation_date', 'expire_date')
    list_filter = ['creation_date']
    search_fields = ['title']
    date_hierarchy = 'creation_date'

    fieldsets = [
        (None, {'fields': ['title']}),
        ('Date information', {'fields': ['creation_date', 'expire_date'], 'classes': ['collapse']}),
        ]
    inlines = [BooleanCheckInline, SingleCheckInline,
               MultipleCheckInline, NumericCheckInline]

admin.site.register(Checklist, ChecklistAdmin)
