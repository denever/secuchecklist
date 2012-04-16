from django import forms
from riskfactors.models import RiskFactor

class RiskFactorForm(forms.ModelForm):
    class Meta:
        model = RiskFactor
