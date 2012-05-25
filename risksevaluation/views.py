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

from django.views.generic.edit import ModelFormMixin, ProcessFormView
from django.views.generic.detail import SingleObjectTemplateResponseMixin

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
        self.risksevaluationdocument.company = get_object_or_404(CustomerCompany,
                                                                 id=self.kwargs['company'])
        self.risksevaluationdocument.revision = get_object_or_404(Revision,
                                                                  id=self.kwargs['change'])
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


class RiskFactorEvaluationView(SingleObjectTemplateResponseMixin, ModelFormMixin, ProcessFormView):
    form_class = RiskFactorEvaluationForm
    template_name = 'risksevaluation/riskevaluation_create_form.html'
    success_url = '/risksevaluation/%(company)/revision/%(revision)/eval/%(riskfactor)'

    def get_context_data(self, **kwargs):
        context = super(RiskFactorEvaluationView, self).get_context_data(**kwargs)
        context['document'] = get_object_or_404(RisksEvaluationDocument,
                                                    revision=self.kwargs['revision'])
        context['riskfactor'] = get_object_or_404(RiskFactor,
                                                  id=self.kwargs['riskfactor'])
        context['company'] = get_object_or_404(CustomerCompany,
                                               id=self.kwargs['company'])
        return context

    def get(self, request, *args, **kwargs):
        document_id = self.kwargs['revision']
        risk_factor_id = self.kwargs['riskfactor']
        try:
            self.object = RiskFactorEvaluation.objects.get(document_id=document_id,
                                                   risk_factor_id=risk_factor_id)
        except:
            self.object = None
        return super(RiskFactorEvaluationView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        document_id = self.kwargs['revision']
        risk_factor_id = self.kwargs['riskfactor']
        try:
            self.object = RiskFactorEvaluation.objects.get(document_id=document_id,
                                                   risk_factor_id=risk_factor_id)
        except:
            self.object = None
        return super(RiskFactorEvaluationView, self).post(request, *args, **kwargs)

class EvalRiskFactorStatusView(View):
    def get(self, request, *args, **kwargs):
        pass

    def post(self, request, *args, **kwargs):
        document = get_object_or_404(RisksEvaluationDocument,
                                     revision=self.request.POST['revision_id'])
        riskfactor = get_object_or_404(RiskFactor,
                                       id=self.request.POST['riskfactor_id'] )
        try:
            rfe = RiskFactorEvaluation.objects.get(document=document,
                                                   risk_factor=riskfactor)
            rfe.status = self.request.POST['status']
            rfe.lastupdate_by = self.request.user.get_profile()
            rfe.save()
        except:
            rfe = RiskFactorEvaluation(document=document,
                                       risk_factor=riskfactor,
                                       status=self.request.POST['status'])
            rfe.record_by = self.request.user.get_profile()
            rfe.lastupdate_by = self.request.user.get_profile()
            rfe.save()
        return HttpResponse('Ok')

class EvalRiskFactorProbabilityView(View):
    def get(self, request, *args, **kwargs):
        pass

    def post(self, request, *args, **kwargs):
        document = get_object_or_404(RisksEvaluationDocument,
                                     revision=self.request.POST['revision_id'])
        riskfactor = get_object_or_404(RiskFactor,
                                       id=self.request.POST['riskfactor_id'])

        rfe = RiskFactorEvaluation.objects.get(document=document,
                                               risk_factor=riskfactor)
        rfe.probability = self.request.POST['probability']
        rfe.lastupdate_by = self.request.user.get_profile()
        rfe.save()
        return HttpResponse('Ok')

class EvalRiskFactorSeriousnessView(View):
    def get(self, request, *args, **kwargs):
        pass

    def post(self, request, *args, **kwargs):
        document = get_object_or_404(RisksEvaluationDocument,
                                     revision=self.request.POST['revision_id'])
        riskfactor = get_object_or_404(RiskFactor,
                                       id=self.request.POST['riskfactor_id'])

        rfe = RiskFactorEvaluation.objects.get(document=document,
                                               risk_factor=riskfactor)
        rfe.seriousness = self.request.POST['seriousness']
        rfe.lastupdate_by = self.request.user.get_profile()
        rfe.save()
        return HttpResponse('Ok')

class TakeMeasureView(View):
    def get(self, request, *args, **kwargs):
        pass

    def post(self, request, *args, **kwargs):
        document = get_object_or_404(RisksEvaluationDocument,
                                     revision=self.request.POST['revision_id'])
        riskfactor = get_object_or_404(RiskFactor,
                                       id=self.request.POST['riskfactor_id'] )
        try:
            rfe = RiskFactorEvaluation.objects.get(document=document,
                                                   risk_factor=riskfactor)
            rfe.measure_taken = True
            rfe.lastupdate_by = self.request.user.get_profile()
            rfe.save()
        except:
            rfe = RiskFactorEvaluation(document=document, risk_factor=riskfactor, measure_taken=True)
            rfe.record_by = self.request.user.get_profile()
            rfe.lastupdate_by = self.request.user.get_profile()
            rfe.save()
        return HttpResponse('Ok')

class UntakeMeasureView(View):
    def get(self, request, *args, **kwargs):
        pass

    def post(self, request, *args, **kwargs):
        document = get_object_or_404(RisksEvaluationDocument,
                                     revision=self.request.POST['revision_id'])
        riskfactor = get_object_or_404(RiskFactor,
                                       id=self.request.POST['riskfactor_id'])

        rfe = RiskFactorEvaluation.objects.get(document=document,
                                               risk_factor=riskfactor)
        rfe.measure_taken = False
        rfe.lastupdate_by = self.request.user.get_profile()
        rfe.save()
        return HttpResponse('Ok')
