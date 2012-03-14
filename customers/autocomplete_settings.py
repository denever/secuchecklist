from autocomplete.views import autocomplete
# Settings for django-autocomplete
from django.db.models import Count

from customers.models import AtecoSector, CPISettlement, TownShip
from autocomplete.views import AutocompleteSettings

class AtecoSectorAutocomplete(AutocompleteSettings):
    queryset = AtecoSector.objects.all()
    search_fields = ('name',)
    login_required = True

class CPISettlementAutocomplete(AutocompleteSettings):
    queryset = CPISettlement.objects.all()
    search_fields = ('name',)
    login_required = True

class TownShipNameAutocomplete(AutocompleteSettings):
    queryset = TownShip.objects.all()
    search_fields = ('^name',)
    value = 'name'
    label = 'name'
    key = 'name'
    login_required = True

class ZipCodeAutocomplete(AutocompleteSettings):
    queryset = TownShip.objects.all()
    search_fields = ('^zipcode',)
    value = 'zipcode'
    label = 'zipcode'
    key = 'zipcode'
    login_required = True

class ProvinceAutocomplete(AutocompleteSettings):
    queryset = TownShip.objects.all()
    search_fields = ('province',)
    value = 'province'
    label = 'province'
    key = 'province'
    login_required = True


autocomplete.register('atecosector', AtecoSectorAutocomplete)
autocomplete.register('cpisettlement', CPISettlementAutocomplete)
autocomplete.register('town', TownShipNameAutocomplete)
autocomplete.register('zipcode', ZipCodeAutocomplete)
autocomplete.register('province', ProvinceAutocomplete)
