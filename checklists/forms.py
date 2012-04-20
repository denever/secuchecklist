from django import forms
from checklists.models import CheckList, RiskFactorEvaluation

class CheckListForm(forms.ModelForm):
    class Meta:
        model = CheckList


class RiskFactorEvaluationForm(forms.ModelForm):
    class Meta:
        model = RiskFactorEvaluation
