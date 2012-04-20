from customers.models import *

from django.contrib import admin

admin.site.register(Province)
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
admin.site.register(Equipment)
admin.site.register(DPI)

class TownShipAdmin(admin.ModelAdmin):
    list_display = ('name', 'province', 'zipcode')
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

# import reversion

# class CustomerCompanyRevAdmin(reversion.VersionAdmin):
#     pass

# admin.site.register(CustomerCompany, CustomerCompanyRevAdmin)
