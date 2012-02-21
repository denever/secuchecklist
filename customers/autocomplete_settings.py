from autocomplete.views import autocomplete
# Settings for django-autocomplete

from customers.models import AtecoSector, CPISettlement
from autocomplete.views import AutocompleteSettings

class AtecoSectorAutocomplete(AutocompleteSettings):
    queryset = AtecoSector.objects.all()
    search_fields = ('^name',)
    login_required = True

class CPISettlementAutocomplete(AutocompleteSettings):
    queryset = CPISettlement.objects.all()
    search_fields = ('^name',)
    login_required = True


autocomplete.register('atecosector', AtecoSectorAutocomplete)
autocomplete.register('cpisettlement', CPISettlementAutocomplete)
