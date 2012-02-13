from django import forms
from django.contrib.localflavor.it.forms import ITSocialSecurityNumberField, ITVatNumberField
from itphone_field import ITPhoneNumberField
from customers.models import CustomerCompany, Staff
from django.contrib.admin import widgets

class CustomerCompanyForm(forms.ModelForm):
    tax_code = ITSocialSecurityNumberField()
    vat_code = ITVatNumberField()
    phone = ITPhoneNumberField()
    fax = ITPhoneNumberField()

    class Meta:
        model = CustomerCompany
        exclude = ('record_by')

class StaffForm(forms.ModelForm):
    phone = ITPhoneNumberField()
    
    class Meta:
        model = Staff
        widgets = {'birth_date': widgets.AdminDateWidget(),
                   'employ_date':widgets.AdminDateWidget(),
                   }
