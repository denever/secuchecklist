from checklists.models import Azienda
from checklists.models import Lavoratore
from checklists.models import FiguraPrevenzione
from checklists.models import MansioneOmogenea
from checklists.models import FigureAziendaPrevenzione
from checklists.models import SettoreAteco

from django.contrib import admin

admin.site.register(FiguraPrevenzione)
admin.site.register(MansioneOmogenea)
admin.site.register(SettoreAteco)

class LavoratoreAdmin(admin.ModelAdmin):
    list_display = ('cognome', 'nome', 'mansione_omogenea')
    list_filter = ['cognome', 'nome', 'mansione_omogenea']
    search_fields = ['cognome', 'nome', 'mansione_omogenea']
    date_hierarchy = 'data_nascita'

    fieldsets = [
        (None, {'fields': ['azienda',
                           'cognome',
                           'nome',
                           'data_nascita',
                           'sesso',
                           'mansione',
                           'mansione_omogenea',
                           'reparto',
                           'nazionalita',
                           'forma_contrattuale',
                           'sorveglianza_sanitaria',
                           'computo_lavoratori'
                           ]
                }
         )
        ]

admin.site.register(Lavoratore, LavoratoreAdmin)

class FigureAziendaPrevenzioneAdmin(admin.ModelAdmin):
    list_display = ('cognome', 'nome', 'figura')
    list_filter = ['cognome', 'nome', 'figura']
    search_fields = ['cognome', 'nome', 'figura']
    date_hierarchy = 'data_nascita'

    fieldsets = [
        (None, {'fields': ['azienda',
                           'figura',
                           'cognome',
                           'nome',
                           'data_nascita',
                           'telefono',
                           ]
                }
         )
        ]

admin.site.register(FigureAziendaPrevenzione, FigureAziendaPrevenzioneAdmin)

class AziendaAdmin(admin.ModelAdmin):
    list_display = ('ragione_sociale', 'data_registrazione')
    list_filter = ['data_registrazione']
    search_fields = ['ragione_sociale']
    date_hierarchy = 'data_registrazione'

    fieldsets = [
        (None, {'fields': ['ragione_sociale',
                           'data_registrazione',
                           'telefono',
                           'fax',
                           'email'
                           ]
                }
         ),
        ('Dati legali', {'fields': ['sede_legale_amministrativa',
                                    'sede_insediamento_produttivo',
                                    'iscrizione_ciiaa',
                                    'codice_fiscale',
                                    'partita_iva',
                                    'posizione_inail',
                                    'posizione_inps',
                                    'ccnl',
                                    'settore_ateco',
                                    'certificazioni'
                                    ],
                          'classes': ['collapse']
                         }
         ),
        ('Insediamento', {'fields': ['superficie_insediamento',
                                     'cpi',
                                     'uso_macchine',
                                     'sostanze_pericolose',
                                     'sorveglianza_sanitaria'
                                     ],
                          'classes': ['collapse']
                          }
         )
        ]

admin.site.register(Azienda, AziendaAdmin)
