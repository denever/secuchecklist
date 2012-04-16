# Create your views here.
from riskfactors.models import RiskFactor

from django.views.generic import View
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView
from django.views.generic import TemplateView

from django.shortcuts import get_object_or_404

from django.views.generic.detail import BaseDetailView

from riskfactors.jsonresponsemixin import RiskFactorNodeMixin
from riskfactors.jsonresponsemixin import RiskFactorSubTreeMixin

from riskfactors.forms import RiskFactorForm

class RiskFactorTreeView(TemplateView):
    template_name = 'riskfactors/riskfactor_tree.html'

class RiskFactorDetailView(DetailView):
    model = RiskFactor

class RiskFactorCreateView(CreateView):
    form_class = RiskFactorForm
    template_name = 'riskfactors/riskfactor_create_form.html'
    success_url = '/riskfactors/'

    def get_initial(self):
	self.initial = super(RiskFactorCreateView, self).get_initial()        
	if self.kwargs.has_key('pk'):
            self.initial['parent'] = get_object_or_404(RiskFactor, id=self.kwargs['pk'])
        return self.initial

    # def form_valid(self, form):
    #     return super(RiskFactorCreateView, self).form_valid(form)

class RiskFactorUpdateView(UpdateView):
    model = RiskFactor
    form_class = RiskFactorForm
    template_name = 'riskfactors/riskfactor_update_form.html'
    success_url = '/riskfactors/'

class RiskFactorDeleteView(DeleteView):
    model = RiskFactor
    form_class = RiskFactorForm
    success_url = '/riskfactors/'

class RiskFactorNodeJson(RiskFactorNodeMixin, BaseDetailView):
	model = RiskFactor
    # def get_queryset(self):
    #     parent = get_object_or_404(RiskFactor, id=self.kwargs['pk'])
    #     return RiskFactor.objects.filter(parent__exact=parent)
    #     if self.kwargs['pk'] == '0':
    #         return RiskFactor.objects.filter(parent__exact=None)

class RiskFactorSubTreeJson(RiskFactorSubTreeMixin, BaseDetailView):

    def get_queryset(self):
	if self.kwargs['pk'] == '0':
	    return RiskFactor.objects.filter(parent__exact=None)
	parent = get_object_or_404(RiskFactor, id=self.kwargs['pk'])
	return RiskFactor.objects.filter(parent__exact=parent)
