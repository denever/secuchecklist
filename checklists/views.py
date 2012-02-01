from checklists.models import Azienda
from django.http import HttpResponse

# Create your views here.

def index(request):
    aziende = Azienda.objects.all().order_by('-data_registrazione')
    output = ','.join([str(azienda) for azienda in aziende])
    return HttpResponse(output)

def azienda(request, azienda_id):
    return HttpResponse('Mostra azienda e sue checklist')

def reparti(request, azienda_id):
    return HttpResponse('Mostra i reparti di una azienda')
