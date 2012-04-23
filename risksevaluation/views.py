# Create your views here.
from risksevaluation.models import RisksEvaluationDocument, RiskFactorEvaluation
from customers.models import CustomerCompany

from django.views.generic import View
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView
from django.views.generic import TemplateView

from django.shortcuts import get_object_or_404
from django.core.urlresolvers import reverse

from risksevaluation.forms import RisksEvaluationDocumentForm, RiskFactorEvaluationForm

class RisksEvaluationDocumentDetailView(DetailView):
    model = RisksEvaluationDocument
    context_object_name = 'red'
    
    def get_context_data(self, **kwargs):
        if self.kwargs.has_key('company'):
            context = super(RisksEvaluationDocumentDetailView, self).get_context_data(**kwargs)
            context['company'] = get_object_or_404(CustomerCompany, id=self.kwargs['company'])
            return context

class RisksEvaluationDocumentCreateView(CreateView):
    form_class = RisksEvaluationDocumentForm
    template_name = 'risksevaluation/risksevaluationdocument_create_form.html'
    success_url = '/risksevaluation/'
    context_object_name = 'risksevaluationdocument'

    def form_valid(self, form):
        self.risksevaluationdocument = form.save(commit=False)
        self.risksevaluationdocument.record_by = self.request.user.get_profile()
        self.risksevaluationdocument.lastupdate_by = self.request.user.get_profile()
        self.risksevaluationdocument.company = get_object_or_404(CustomerCompany, id=self.kwargs['company'])
        self.success_url = reverse('red-list', args=self.kwargs['company'])
        return super(RisksEvaluationDocumentCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        if self.kwargs.has_key('company'):
            context = super(RisksEvaluationDocumentCreateView, self).get_context_data(**kwargs)
            context['company'] = get_object_or_404(CustomerCompany, id=self.kwargs['company'])
            return context

class RisksEvaluationDocumentUpdateView(UpdateView):
    model = RisksEvaluationDocument
    form_class = RisksEvaluationDocumentForm
    template_name = 'risksevaluation/risksevaluationdocument_update_form.html'
    success_url = '/risksevaluation/'

    def form_valid(self, form):
        self.risksevaluationdocument = form.save(commit=False)
        self.risksevaluationdocument.lastupdate_by = self.request.user.get_profile()
        self.success_url = reverse('red-detail', args=self.kwargs['company'])
        return super(RisksEvaluationDocumentUpdateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        if self.kwargs.has_key('company'):
            context = super(RisksEvaluationDocumentUpdateView, self).get_context_data(**kwargs)
            context['company'] = get_object_or_404(CustomerCompany, id=self.kwargs['company'])
            return context

class RisksEvaluationDocumentDeleteView(DeleteView):
    model = RisksEvaluationDocument
    form_class = RisksEvaluationDocumentForm
    success_url = '/risksevaluation/'

    def get_context_data(self, **kwargs):
        if self.kwargs.has_key('company'):
            context = super(RisksEvaluationDocumentDeleteView, self).get_context_data(**kwargs)
            context['company'] = get_object_or_404(CustomerCompany, id=self.kwargs['company'])
            return context

class RisksEvaluationDocumentListView(ListView):
    context_object_name = 'reds' # Risks Evaluation DocumentS

    def get_queryset(self):
        if self.kwargs.has_key('company'):
            company = get_object_or_404(CustomerCompany, id=self.kwargs['company'])
            return company.risksevaluationdocument_set.all()
        else:
            return RisksEvaluationDocument.objects.all()

    def get_context_data(self, **kwargs):
        if self.kwargs.has_key('company'):
            context = super(RisksEvaluationDocumentListView, self).get_context_data(**kwargs)
            context['company'] = get_object_or_404(CustomerCompany, id=self.kwargs['company'])
            return context

class AllRisksEvaluationDocumentView(ListView):
    model = RisksEvaluationDocument
    template_name = 'risksevaluation/risksevaluationdocument_list_all.html'
