# encoding: utf-8

# Create your views here.
from django.shortcuts import get_object_or_404
from django.core.urlresolvers import reverse
from django.views.generic import DetailView
from django.views.generic import ListView
from django.views.generic import TemplateView
from django.views.generic import YearArchiveView
from django.views.generic import MonthArchiveView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView
from django.utils import simplejson

from customers.models import *

from customers.forms import CustomerCompanyForm
from customers.forms import StaffForm
from customers.forms import WorkingEnvironmentForm
from customers.forms import DepartmentForm
from customers.forms import CompanySecurityDutyForm
from customers.forms import EquipmentForm

from accounts.models import Activity

class CustomerCompanyYearView(YearArchiveView):
    queryset = CustomerCompany.objects.all()
    date_field = 'record_date'
    make_object_list = True
    context_object_name = 'companies'

    def get_context_data(self, **kwargs):
        context = super(CustomerCompanyYearView, self).get_context_data(**kwargs)
        context['months'] = [  date.strftime('%b') for date in context['date_list'] ]
        return context

class CustomerCompanyMonthView(MonthArchiveView):
    queryset = CustomerCompany.objects.all()
    date_field = 'record_date'
    make_object_list = True
    context_object_name = 'companies'

    def get_context_data(self, **kwargs):
        context = super(CustomerCompanyMonthView, self).get_context_data(**kwargs)
        context['years'] = [ date.year for date in CustomerCompany.objects.dates('record_date', 'year')]
        return context

class CustomerCompanyListView(ListView):
    queryset = CustomerCompany.objects.all()
    context_object_name = 'companies'

    def get_context_data(self, **kwargs):
        context = super(CustomerCompanyListView, self).get_context_data(**kwargs)
        context['years'] = [ date.year for date in CustomerCompany.objects.dates('record_date', 'year')]
        return context

class CustomerCompanyDetailView(DetailView):
    model = CustomerCompany
    context_object_name = 'company'

class CustomerCompanyCreateView(CreateView):
    form_class = CustomerCompanyForm
    template_name = 'customers/customercompany_create_form.html'
    success_url = '/customers/'

    def form_valid(self, form):
        self.company = form.save(commit=False)
        self.company.record_by = self.request.user.get_profile()
        self.company.lastupdate_by = self.request.user.get_profile()
        return super(CustomerCompanyCreateView, self).form_valid(form)

class CustomerCompanyUpdateView(UpdateView):
    model = CustomerCompany
    form_class = CustomerCompanyForm
    template_name = 'customers/customercompany_update_form.html'
    success_url = '/customers/'
    context_object_name = 'company'

    def form_valid(self, form):
        self.company = form.save(commit=False)
        self.company.lastupdate_by = self.request.user.get_profile()
        self.company.newrevision_needed = True
        self.success_url = reverse('company-detail', args=self.kwargs['pk'])
        return super(CustomerCompanyUpdateView, self).form_valid(form)

    # def get_initial(self):
    #     self.initial = super(CustomerCompanyUpdateView, self).get_initial()
    #     self.initial['ateco_sector'] = self.object.ateco_sector.name
    #     self.initial['cpi'] = self.object.cpi.name
    #     return self.initial

class CustomerCompanyDeleteView(DeleteView):
    model = CustomerCompany
    form_class = CustomerCompanyForm
    success_url = '/customers/'
    context_object_name = 'company'

class StaffCreateView(CreateView):
    form_class = StaffForm
    template_name = 'customers/staff_create_form.html'

    def get_context_data(self, **kwargs):
        context = super(StaffCreateView, self).get_context_data(**kwargs)
        context['company'] = get_object_or_404(CustomerCompany, id=self.kwargs['company'])
        context['form'].fields['department'].queryset = Department.objects.filter(company=context['company'])
        return context

    def form_valid(self, form):
        self.staff = form.save(commit=False)
        self.staff.record_by = self.request.user.get_profile()
        self.staff.lastupdate_by = self.request.user.get_profile()
        self.staff.company = get_object_or_404(CustomerCompany, id=self.kwargs['company'])
        self.staff.company.newrevision_needed = True
        self.success_url = reverse('staff-list', args=self.kwargs['company'])
        return super(StaffCreateView, self).form_valid(form)

class StaffListView(ListView):
    context_object_name = 'staff_set'

    def get_queryset(self):
        company = get_object_or_404(CustomerCompany, id=self.kwargs['company'])
        return company.staff_set.all()

    def get_context_data(self, **kwargs):
        context = super(StaffListView, self).get_context_data(**kwargs)
        context['company'] = get_object_or_404(CustomerCompany, id=self.kwargs['company'])
        return context

class StaffDetailView(DetailView):
    model = Staff
    context_object_name = 'staff'

    def get_context_data(self, **kwargs):
        context = super(StaffDetailView, self).get_context_data(**kwargs)
        context['company'] = get_object_or_404(CustomerCompany, id=self.kwargs['company'])
        return context

class StaffUpdateView(UpdateView):
    model = Staff
    form_class = StaffForm
    template_name = 'customers/staff_update_form.html'
    success_url = '/customers/'

    def get_context_data(self, **kwargs):
        context = super(StaffUpdateView, self).get_context_data(**kwargs)
        context['company'] = get_object_or_404(CustomerCompany, id=self.kwargs['company'])
        return context

    def form_valid(self, form):
        self.staff = form.save(commit=False)
        self.staff.lastupdate_by = self.request.user.get_profile()
        self.staff.company.newrevision_needed = True
        self.success_url = reverse('staff-detail', args=self.kwargs['company'])
        return super(StaffUpdateView, self).form_valid(form)

class StaffDeleteView(DeleteView):
    model = Staff
    form_class = StaffForm
    success_url = '/customers/'

    def get_context_data(self, **kwargs):
        context = super(StaffDeleteView, self).get_context_data(**kwargs)
        context['company'] = get_object_or_404(CustomerCompany, id=self.kwargs['company'])
        return context

    def get_success_url(self):
        return reverse('staff-list', args=self.kwargs['company'])

class WorkingEnvironmentEditView(UpdateView):
    form_class = WorkingEnvironmentForm
    model = CustomerCompany
    template_name = 'customers/workingenvironment_create_form.html'
    success_url = '/customers/'
    context_object_name = 'company'

    def form_valid(self, form):
        self.company = form.save(commit=False)
        self.company.lastupdate_by = self.request.user.get_profile()
        self.company.newrevision_needed = True
        self.success_url = reverse('set-working-env', args=[self.kwargs['pk']])
        return super(WorkingEnvironmentEditView, self).form_valid(form)

class DepartmentCreateView(CreateView):
    form_class = DepartmentForm
    template_name = 'customers/department_create_form.html'

    def form_valid(self, form):
        self.department = form.save(commit=False)
        self.department.record_by = self.request.user.get_profile()
        self.department.lastupdate_by = self.request.user.get_profile()
        self.department.company = get_object_or_404(CustomerCompany, id=self.kwargs['company'])
        self.department.company.newrevision_needed = True
        self.success_url = reverse('set-working-env', args=self.kwargs['company'])
        return super(DepartmentCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(DepartmentCreateView, self).get_context_data(**kwargs)
        context['company'] = get_object_or_404(CustomerCompany, id=self.kwargs['company'])
        return context

class DepartmentDetailView(DetailView):
    model = Department
    context_object_name = 'department'

    def get_context_data(self, **kwargs):
        context = super(DepartmentDetailView, self).get_context_data(**kwargs)
        context['company'] = get_object_or_404(CustomerCompany, id=self.kwargs['company'])
        return context

class DepartmentUpdateView(UpdateView):
    model = Department
    form_class = DepartmentForm
    template_name = 'customers/department_update_form.html'
    success_url = '/customers/'

    def form_valid(self, form):
        self.department = form.save(commit=False)
        self.department.lastupdate_by = self.request.user.get_profile()
        self.department.company.newrevision_needed = True
        self.success_url = reverse('department-detail', args=[self.kwargs['company'],
                                                              self.department.id])
        return super(DepartmentUpdateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(DepartmentUpdateView, self).get_context_data(**kwargs)
        context['company'] = get_object_or_404(CustomerCompany, id=self.kwargs['company'])
        return context

class DepartmentDeleteView(DeleteView):
    model = Department
    form_class = DepartmentForm
    success_url = '/customers/'

    def get_context_data(self, **kwargs):
        context = super(DepartmentDeleteView, self).get_context_data(**kwargs)
        context['company'] = get_object_or_404(CustomerCompany, id=self.kwargs['company'])
        return context

    def get_success_url(self):
        return reverse('set-working-env', args=self.kwargs['company'])

class CompanySecurityDutyCreateView(CreateView):
    form_class = CompanySecurityDutyForm
    template_name = 'customers/companysecurityduty_create_form.html'

    def get_context_data(self, **kwargs):
        context = super(CompanySecurityDutyCreateView, self).get_context_data(**kwargs)
        context['company'] = get_object_or_404(CustomerCompany, id=self.kwargs['company'])
        return context

    def form_valid(self, form):
        self.companysecurityduty = form.save(commit=False)
        self.companysecurityduty.record_by = self.request.user.get_profile()
        self.companysecurityduty.lastupdate_by = self.request.user.get_profile()
        self.companysecurityduty.company = get_object_or_404(CustomerCompany,
                                                             id=self.kwargs['company'])
        self.companysecurityduty.company.newrevision_needed = True
        self.success_url = reverse('companysecurityduty-list', args=self.kwargs['company'])
        return super(CompanySecurityDutyCreateView, self).form_valid(form)

class CompanySecurityDutyListView(ListView):
    context_object_name = 'companysecurityduty_set'

    def get_queryset(self):
        company = get_object_or_404(CustomerCompany, id=self.kwargs['company'])
        return company.companysecurityduty_set.all()

    def get_context_data(self, **kwargs):
        context = super(CompanySecurityDutyListView, self).get_context_data(**kwargs)
        context['company'] = get_object_or_404(CustomerCompany, id=self.kwargs['company'])
        return context

class CompanySecurityDutyUpdateView(UpdateView):
    model = CompanySecurityDuty
    form_class = CompanySecurityDutyForm
    template_name = 'customers/companysecurityduty_update_form.html'
    success_url = '/customers/'

    def get_context_data(self, **kwargs):
        context = super(CompanySecurityDutyUpdateView, self).get_context_data(**kwargs)
        context['company'] = get_object_or_404(CustomerCompany, id=self.kwargs['company'])
        return context

    def form_valid(self, form):
        self.companysecurityduty = form.save(commit=False)
        self.companysecurityduty.lastupdate_by = self.request.user.get_profile()
        self.companysecurityduty.company.newrevision_needed = True
        self.success_url = reverse('companysecurityduty-list', args=self.kwargs['company'])
        return super(CompanySecurityDutyUpdateView, self).form_valid(form)

class CompanySecurityDutyDeleteView(DeleteView):
    model = CompanySecurityDuty
    form_class = CompanySecurityDutyForm
    success_url = '/customers/'

    def get_context_data(self, **kwargs):
        context = super(CompanySecurityDutyDeleteView, self).get_context_data(**kwargs)
        context['company'] = get_object_or_404(CustomerCompany, id=self.kwargs['company'])
        return context

    def get_success_url(self):
        return reverse('companysecurityduty-list', args=self.kwargs['company'])

class CompanySecurityDutyDetailView(DetailView):
    model = CompanySecurityDuty

    def get_context_data(self, **kwargs):
        context = super(CompanySecurityDutyDetailView, self).get_context_data(**kwargs)
        context['company'] = get_object_or_404(CustomerCompany, id=self.kwargs['company'])
        return context

class EquipmentCreateView(CreateView):
    form_class = EquipmentForm
    template_name = 'customers/equipment_create_form.html'

    def get_context_data(self, **kwargs):
        context = super(EquipmentCreateView, self).get_context_data(**kwargs)
        context['company'] = get_object_or_404(CustomerCompany, id=self.kwargs['company'])
        context['form'].fields['department'].queryset = Department.objects.filter(company=context['company'])
        context['form'].fields['operator'].queryset = Staff.objects.filter(company=context['company'])
        context['form'].fields['exposed_staff'].queryset = Staff.objects.filter(company=context['company'])
        return context

    def form_valid(self, form):
        self.equipment = form.save(commit=False)
        self.equipment.record_by = self.request.user.get_profile()
        self.equipment.lastupdate_by = self.request.user.get_profile()
        self.equipment.company = get_object_or_404(CustomerCompany,
                                                             id=self.kwargs['company'])
        self.equipment.company.newrevision_needed = True
        self.success_url = reverse('equipment-list', args=self.kwargs['company'])
        return super(EquipmentCreateView, self).form_valid(form)

class EquipmentListView(ListView):
    context_object_name = 'equipment_set'

    def get_queryset(self):
        company = get_object_or_404(CustomerCompany, id=self.kwargs['company'])
        deps = company.department_set.all()
        return Equipment.objects.filter(department__in=deps)

    def get_context_data(self, **kwargs):
        context = super(EquipmentListView, self).get_context_data(**kwargs)
        context['company'] = get_object_or_404(CustomerCompany, id=self.kwargs['company'])
        return context

class EquipmentUpdateView(UpdateView):
    model = Equipment
    form_class = EquipmentForm
    template_name = 'customers/equipment_update_form.html'
    success_url = '/customers/'

    def get_context_data(self, **kwargs):
        context = super(EquipmentUpdateView, self).get_context_data(**kwargs)
        context['company'] = get_object_or_404(CustomerCompany, id=self.kwargs['company'])
        context['form'].fields['department'].queryset = Department.objects.filter(company=context['company'])
        context['form'].fields['operator'].queryset = Staff.objects.filter(company=context['company'])
        context['form'].fields['exposed_staff'].queryset = Staff.objects.filter(company=context['company'])
        return context

    def form_valid(self, form):
        self.equipment = form.save(commit=False)
        self.equipment.lastupdate_by = self.request.user.get_profile()
        self.equipment.department.company.newrevision_needed = True
        self.success_url = reverse('equipment-list', args=self.kwargs['company'])
        return super(EquipmentUpdateView, self).form_valid(form)

class EquipmentDeleteView(DeleteView):
    model = Equipment
    form_class = EquipmentForm
    success_url = '/customers/'

    def get_context_data(self, **kwargs):
        context = super(EquipmentDeleteView, self).get_context_data(**kwargs)
        context['company'] = get_object_or_404(CustomerCompany, id=self.kwargs['company'])
        return context

    def get_success_url(self):
        return reverse('equipment-list', args=self.kwargs['company'])

class EquipmentDetailView(DetailView):
    model = Equipment

    def get_context_data(self, **kwargs):
        context = super(EquipmentDetailView, self).get_context_data(**kwargs)
        context['company'] = get_object_or_404(CustomerCompany, id=self.kwargs['company'])
        return context

class ChangesListView(ListView):
    context_object_name = 'changes'
    template_name = 'customers/changes_list.html'

    def get_queryset(self):
        company = get_object_or_404(CustomerCompany, id=self.kwargs['company'])
        return company.get_changes()

    def get_context_data(self, **kwargs):
        context = super(ChangesListView, self).get_context_data(**kwargs)
        context['company'] = get_object_or_404(CustomerCompany, id=self.kwargs['company'])
        return context

class ChangeDetailView(DetailView):
    model = Activity
    context_object_name = 'change'
    template_name = 'customers/change_detail.html'

    def get_context_data(self, **kwargs):
        context = super(ChangeDetailView, self).get_context_data(**kwargs)
        context['company'] = get_object_or_404(CustomerCompany, id=self.kwargs['company'])
        change = context['change']
        try:
            context['diff_list'] = simplejson.loads(change.serialized_data)
        except Exception, e:
            print e
        return context
