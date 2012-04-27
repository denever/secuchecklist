# Create your views here.
from risksevaluation.models import RisksEvaluationDocument, RiskFactorEvaluation
from customers.models import CustomerCompany
from riskfactors.models import RiskFactor

from django.views.generic import View
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView
from django.views.generic import TemplateView

from django.shortcuts import get_object_or_404
from django.core.urlresolvers import reverse
from django.http import HttpResponse

from risksevaluation.forms import RisksEvaluationDocumentForm, RiskFactorEvaluationForm

class RisksEvaluationDocumentDetailView(DetailView):
    model = RisksEvaluationDocument
    context_object_name = 'red'

    def get_context_data(self, **kwargs):
        if self.kwargs.has_key('company'):
#            print self.request.GET['id']
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
        self.success_url = reverse('red-detail', args=[self.kwargs['company'],
                                                       self.kwargs['pk']])
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

# class RiskEvaluationView(View):
#     def get(self, request, *args):
#         rfef = RiskFactorEvaluationForm()
#         return HttpResponse(rfef.as_table())

class RiskEvaluationCreateView(CreateView):
    form_class = RiskFactorEvaluationForm
    template_name = 'risksevaluation/riskevaluation_create_form.html'
    success_url = '/risksevaluation/%(company)/revision/%(revision)/eval/%(riskfactor)'

    def form_valid(self, form):
        self.riskevaluation = form.save(commit=False)
        self.riskevaluation.record_by = self.request.user.get_profile()
        self.riskevaluation.lastupdate_by = self.request.user.get_profile()
        self.riskevaluation.document = get_object_or_404(RisksEvaluationDocument,
                                                         revision=self.kwargs['revision'])
        self.riskevaluation.risk_factor = get_object_or_404(RiskFactor,
                                                            id=self.kwargs['riskfactor'])
        self.success_url = reverse('red-detail', args=[self.kwargs['company'],
                                                       self.kwargs['revision']])
        return super(RiskEvaluationCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        if self.kwargs.has_key('company'):
            context = super(RiskEvaluationCreateView, self).get_context_data(**kwargs)
            context['document'] = get_object_or_404(RisksEvaluationDocument,
                                                    revision=self.kwargs['revision'])
            context['riskfactor'] = get_object_or_404(RiskFactor,
                                                       id=self.kwargs['riskfactor'])
            context['company'] = get_object_or_404(CustomerCompany,
                                                   id=self.kwargs['company'])
            return context

    # def get_initial(self):
    #     self.initial = super(RiskEvaluationCreateView, self).get_initial()
    #     self.initial['document'] = get_object_or_404(RisksEvaluationDocument,
    #                                                  revision=self.kwargs['document'])
    #     self.initial['riskfactor'] =
    #                                                  id=self.kwargs['riskfactor'])
    #     return self.initial

# class CheckRiskFactor(View):
#     def post(self, request, *args):
#         company_id = request.POST['company'];
#         revision_id = request.POST['revision'];
#         riskfactor_id = request.POST['riskfactor'];

#         rfe = RiskFactorEvaluation(document=get_object_or_404(RisksEvaluationDocument,
#                                                               revision=revision_id),
#                                    risk_factor=get_object_or_404(RiskFactor, id=riskfactor_id),
#                                    record_by = self.request.user.get_profile(),
#                                    lastupdate_by = self.request.user.get_profile())
#         rfe.save()
#         return HttpResponse('Ok',
#                             content_type='application/json')
