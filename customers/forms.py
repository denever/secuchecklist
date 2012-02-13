from django import forms
from django.contrib.localflavor.it.forms import ITSocialSecurityNumberField, ITVatNumberField
from customers.widgets import ITPhoneNumberField
from customers.models import CustomerCompany, Staff, Nationality
from django.contrib.admin import widgets

class CustomerCompanyForm(forms.ModelForm):
    tax_code = ITSocialSecurityNumberField(label='Codice Fiscale')
    vat_code = ITVatNumberField(label='Partita IVA')
    phone = ITPhoneNumberField(label='Telefono')
    fax = ITPhoneNumberField(label='Fax')

    class Meta:
        model = CustomerCompany
        fields = ('record_by',
                  'firm',
                  'phone',
                  'fax',
                  'email',
                  'registered_office',
                  'settlement',
                  'ciiaa',
                  'tax_code',
                  'vat_code',
                  'inail_pos',
                  'inps_pos',
                  'ccnl',
                  'ateco_sector',
                  'certifications',
                  'settlement_size',
                  'cpi',
                  'machine_use',
                  'dangerous_substances',
                  'health_surveillance')
        
class StaffForm(forms.ModelForm):
    phone = ITPhoneNumberField(label='Telefono', required=False)

    class Meta:
        model = Staff
        widgets = {'birth_date': widgets.AdminDateWidget(),
                   'employ_date': widgets.AdminDateWidget(),
                   }
