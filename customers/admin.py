from customers.models import TownShip
from customers.models import AtecoSector
from customers.models import StandardTask
from customers.models import Role
from customers.models import SecurityDuty
from customers.models import Certification
from customers.models import Department
from customers.models import Nationality
from customers.models import CollaborationAgreement
from customers.models import Staff
from customers.models import CustomerCompany
from customers.models import HealthSurveillance
from customers.models import CPISettlement
from customers.models import CompanySecurityDuty

from django.contrib import admin

admin.site.register(AtecoSector)
admin.site.register(StandardTask)
admin.site.register(Role)
admin.site.register(SecurityDuty)
admin.site.register(Certification)
admin.site.register(Department)
admin.site.register(Nationality)
admin.site.register(CollaborationAgreement)
admin.site.register(HealthSurveillance)
admin.site.register(CPISettlement)
admin.site.register(CompanySecurityDuty)

class TownShipAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'province', 'zipcode')
    list_filter = ['zipcode']
    search_field = ['name', 'zipcode']

admin.site.register(TownShip, TownShipAdmin)

class StaffAdmin(admin.ModelAdmin):
    list_display = ('surname', 'name') #, 'mansione_omogenea')
    list_filter = ['surname', 'name'] #, 'mansione_omogenea']
    search_fields = ['surname', 'name'] #, 'mansione_omogenea']
    date_hierarchy = 'birth_date'

    fieldsets = [
        (None, {'fields': ['surname',
                           'name',
                           'birth_date',
                           'gender',
                           'nationality',
                           'employ_date',
                           'collagreement',
                           'health_surveillance',
                           'workers_count',
                           'company',
                           'standard_task',
                           'department',
                           'role',
                           ]
                }
         ),
        ]

admin.site.register(Staff, StaffAdmin)

class CustomerCompanyAdmin(admin.ModelAdmin):
    list_display = ('firm', 'record_date')
    list_filter = ['record_date']
    search_fields = ['firm']
    date_hierarchy = 'record_date'

    fieldsets = [
        (None, {'fields': ['record_by',
                           'firm',
                           'phone',
                           'fax',
                           'email'
                           ]
                }
         ),
        ('Dati legali', {'fields': ['registered_office',
                                    'settlement',
                                    'ciiaa',
                                    'tax_code',
                                    'vat_code',
                                    'inail_pos',
                                    'inps_pos',
                                    'ccnl',
                                    'ateco_sector',
                                    'certifications'
                                    ],
                          'classes': ['collapse']
                         }
         ),
        ('Insediamento', {'fields': ['settlement_size',
                                     'cpi',
                                     'machine_use',
                                     'dangerous_substances',
                                     'health_surveillance'
                                     ],
                          'classes': ['collapse']
                          }
         ),
        ]

admin.site.register(CustomerCompany, CustomerCompanyAdmin)
