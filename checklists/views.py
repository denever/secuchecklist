# Create your views here.
from checklists.models import RiskFactor

from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic.list import BaseListView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView
from django.views.generic import TemplateView

from checklists.jsonresponsemixin import RiskFactorJsonResponseMixin

class RiskFactorTreeView(TemplateView):
    template_name = 'checklists/riskfactor_tree.html'

class RiskFactorDetailView(DetailView):
    model = RiskFactor

class RiskFactorCreateView(CreateView):
    pass

class RiskFactorUpdateView(UpdateView):
    pass

class RiskFactorDeleteView(DeleteView):
    pass

class RiskFactorJSONDetailView(RiskFactorJsonResponseMixin, BaseListView):
    queryset = RiskFactor.objects.filter(parent__exact=None)

    def get_queryset(self):
        print self.kwargs
        return RiskFactor.objects.filter(parent__exact=None)
