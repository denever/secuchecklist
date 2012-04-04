# Create your views here.
from checklists.models import RiskFactor

from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic.list import BaseListView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView
from django.views.generic import TemplateView

from checklists.jsonresponsemixin import JSONResponseMixin

class RiskFactorTreeView(TemplateView):
    template_name = 'checklists/riskfactor_tree.html'

class RiskFactorDetailView(DetailView):
    pass

class RiskFactorCreateView(CreateView):
    pass

class RiskFactorUpdateView(UpdateView):
    pass

class RiskFactorDeleteView(DeleteView):
    pass

class RiskFactorJSONDetailView(JSONResponseMixin, BaseListView):
    queryset = RiskFactor.objects.filter(parent__exact=None)
