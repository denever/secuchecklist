from django import forms
from django.contrib.admin import widgets
from django.contrib.localflavor.it.forms import ITSocialSecurityNumberField, ITVatNumberField

from customers.widgets import ITPhoneNumberField

from customers.models import CustomerCompany
from customers.models import Staff
from customers.models import Nationality
from customers.models import Department
from customers.models import CompanySecurityDuty

# using autocomplete widgets
from autocomplete import widgets as autocomplete_widgets

class CustomerCompanyForm(forms.ModelForm):
    tax_code = ITVatNumberField(label='Codice Fiscale')
    vat_code = ITVatNumberField(label='Partita IVA')
    phone = ITPhoneNumberField(label='Telefono')
    fax = ITPhoneNumberField(label='Fax')

    class Meta:
        model = CustomerCompany
        fields = (
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

        widgets = {'ateco_sector': autocomplete_widgets.AutocompleteWidget('atecosector'),
                   'cpi': autocomplete_widgets.AutocompleteWidget('cpisettlement')
                   }

class StaffForm(forms.ModelForm):
    phone = ITPhoneNumberField(label='Telefono', required=False)

    class Meta:
        model = Staff
        widgets = {'birth_date': widgets.AdminDateWidget(),
                   'employ_date': widgets.AdminDateWidget(),
                   }
        fields = (
                  'surname',
                  'name',
                  'birth_date',
                  'gender',
                  'nationality',
                  'employ_date',
                  'collagreement',
                  'health_surveillance',
                  'workers_count',
                  'standard_task',
                  'department',
                  'role',
                  )

class WorkingEnvironmentForm(forms.ModelForm):
    class Meta:
        model = CustomerCompany
        fields = ('working_environment', )

class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        exclude = ('company', 'record_by', 'lastupdate_by')

class CompanySecurityDutyForm(forms.ModelForm):
    internal_phone = ITPhoneNumberField(label='Telefono interno')
    external_phone = ITPhoneNumberField(label='Telefono esterno')

    class Meta:
        model = CompanySecurityDuty
        exclude = ('company', 'record_by', 'lastupdate_by')
