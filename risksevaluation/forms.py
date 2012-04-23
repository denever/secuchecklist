from django import forms
from checklists.models import Checklist, RiskFactorEvaluation

class ChecklistForm(forms.ModelForm):
    class Meta:
        model = Checklist
        exclude = ('company', 'record_by', 'lastupdate_by')

class RiskFactorEvaluationForm(forms.ModelForm):
    class Meta:
        model = RiskFactorEvaluation
