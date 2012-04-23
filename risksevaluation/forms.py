from django import forms
from risksevaluation.models import RisksEvaluationDocument, RiskFactorEvaluation

class RisksEvaluationDocumentForm(forms.ModelForm):
    class Meta:
        model = RisksEvaluationDocument
        exclude = ('company', 'record_by', 'lastupdate_by')

class RiskFactorEvaluationForm(forms.ModelForm):
    class Meta:
        model = RiskFactorEvaluation
