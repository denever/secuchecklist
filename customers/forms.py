from django import forms
from customers.models import CustomerCompany

class CustomerCompanyForm(forms.ModelForm):
    class Meta:
        model = CustomerCompany
