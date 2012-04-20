# Create your views here.
from checklists.models import CheckList, RiskFactorEvaluation
from customers.models import CustomerCompany

from django.views.generic import View
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView
from django.views.generic import TemplateView

from django.shortcuts import get_object_or_404

from checklists.forms import CheckListForm, RiskFactorEvaluationForm

class CheckListDetailView(DetailView):
    model = CheckList

class CheckListCreateView(CreateView):
    form_class = CheckListForm
    template_name = 'checklists/checklist_create_form.html'
    success_url = '/checklists/'

    def form_valid(self, form):
        self.checklist.record_by = self.request.user.get_profile()
        self.checklist.lastupdate_by = self.request.user.get_profile()
        self.checklist.company = get_object_or_404(CustomerCompany, id=self.kwargs['company'])
        return super(CheckListCreateView, self).form_valid(form)

class CheckListUpdateView(UpdateView):
    model = CheckList
    form_class = CheckListForm
    template_name = 'checklists/checklist_update_form.html'
    success_url = '/checklists/'

    def form_valid(self, form):
        self.checklist.lastupdate_by = self.request.user.get_profile()
        self.success_url = reverse('checklist-detail', args=self.kwargs['company'])
        return super(CheckListUpdateView, self).form_valid(form)

class CheckListDeleteView(DeleteView):
    model = CheckList
    form_class = CheckListForm
    success_url = '/checklists/'

class CheckListListView(ListView):
    context_object_name = 'checklist_set'

    def get_queryset(self):
        if self.kwargs.has_key('company'):
            company = get_object_or_404(CustomerCompany, id=self.kwargs['company'])
            return company.checklist_set.all()
        else:
            return CheckList.objects.all()

    def get_context_data(self, **kwargs):
        if self.kwargs.has_key('company'):
            context = super(CheckListListView, self).get_context_data(**kwargs)
            context['company'] = get_object_or_404(CustomerCompany, id=self.kwargs['company'])
            return context

class AllCheckListView(ListView):
    model = CheckList
