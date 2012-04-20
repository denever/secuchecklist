# Create your views here.
from checklists.models import Checklist, RiskFactorEvaluation
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

from checklists.forms import ChecklistForm, RiskFactorEvaluationForm

class ChecklistDetailView(DetailView):
    model = Checklist

    def get_context_data(self, **kwargs):
        if self.kwargs.has_key('company'):
            context = super(ChecklistDetailView, self).get_context_data(**kwargs)
            context['company'] = get_object_or_404(CustomerCompany, id=self.kwargs['company'])
            return context

class ChecklistCreateView(CreateView):
    form_class = ChecklistForm
    template_name = 'checklists/checklist_create_form.html'
    success_url = '/checklists/'
    context_object_name = 'checklist'

    def form_valid(self, form):
        self.checklist = form.save(commit=False)
        self.checklist.record_by = self.request.user.get_profile()
        self.checklist.lastupdate_by = self.request.user.get_profile()
        self.checklist.company = get_object_or_404(CustomerCompany, id=self.kwargs['company'])
        self.success_url = reverse('checklists-list', args=self.kwargs['company'])
        return super(ChecklistCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        if self.kwargs.has_key('company'):
            context = super(ChecklistCreateView, self).get_context_data(**kwargs)
            context['company'] = get_object_or_404(CustomerCompany, id=self.kwargs['company'])
            return context

class ChecklistUpdateView(UpdateView):
    model = Checklist
    form_class = ChecklistForm
    template_name = 'checklists/checklist_update_form.html'
    success_url = '/checklists/'

    def form_valid(self, form):
        self.checklist = form.save(commit=False)
        self.checklist.lastupdate_by = self.request.user.get_profile()
        self.success_url = reverse('checklist-detail', args=self.kwargs['company'])
        return super(ChecklistUpdateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        if self.kwargs.has_key('company'):
            context = super(ChecklistUpdateView, self).get_context_data(**kwargs)
            context['company'] = get_object_or_404(CustomerCompany, id=self.kwargs['company'])
            return context

class ChecklistDeleteView(DeleteView):
    model = Checklist
    form_class = ChecklistForm
    success_url = '/checklists/'

    def get_context_data(self, **kwargs):
        if self.kwargs.has_key('company'):
            context = super(ChecklistDeleteView, self).get_context_data(**kwargs)
            context['company'] = get_object_or_404(CustomerCompany, id=self.kwargs['company'])
            return context

class ChecklistListView(ListView):
    context_object_name = 'checklists'

    def get_queryset(self):
        if self.kwargs.has_key('company'):
            company = get_object_or_404(CustomerCompany, id=self.kwargs['company'])
            return company.checklist_set.all()
        else:
            return Checklist.objects.all()

    def get_context_data(self, **kwargs):
        if self.kwargs.has_key('company'):
            context = super(ChecklistListView, self).get_context_data(**kwargs)
            context['company'] = get_object_or_404(CustomerCompany, id=self.kwargs['company'])
            return context

class AllChecklistView(ListView):
    model = Checklist
    template_name = 'checklists/checklist_list_all.html'
