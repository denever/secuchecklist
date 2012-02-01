from checklists.models import Azienda
from checklists.models import Lavoratore
from checklists.models import FiguraPrevenzione
from checklists.models import MansioneOmogenea
from checklists.models import FigureAziendaPrevenzione
from checklists.models import SettoreAteco
from checklists.models import Certificazione
from checklists.models import Reparto
from checklists.models import ResultChecklistGenerica
from checklists.models import ResultChecklistReparto
from checklists.models import ResultChecklistMansioneOmogenea

from django.contrib import admin

admin.site.register(FiguraPrevenzione)
admin.site.register(MansioneOmogenea)
admin.site.register(SettoreAteco)
admin.site.register(Certificazione)
admin.site.register(Reparto)
admin.site.register(ResultChecklistGenerica)
admin.site.register(ResultChecklistReparto)
admin.site.register(ResultChecklistMansioneOmogenea)

