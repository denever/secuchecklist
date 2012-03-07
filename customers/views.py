# Create your views here.
from django.shortcuts import get_object_or_404
from django.core.urlresolvers import reverse
from django.views.generic import DetailView
from django.views.generic import ListView
from django.views.generic import YearArchiveView
from django.views.generic import MonthArchiveView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView
from customers.models import *
from customers.forms import CustomerCompanyForm
from customers.forms import StaffForm
from customers.forms import WorkingEnvironmentForm
from customers.forms import DepartmentForm
from customers.forms import CompanySecurityDutyForm

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
	return super(CustomerCompanyCreateView, self).form_valid(form)

class CustomerCompanyUpdateView(UpdateView):
    model = CustomerCompany
    form_class = CustomerCompanyForm
    template_name = 'customers/customercompany_update_form.html'
    success_url = '/customers/'
    context_object_name = 'company'

    def form_valid(self, form):
	self.success_url = reverse('company-detail', args=self.kwargs['pk'])
	return super(CustomerCompanyUpdateView, self).form_valid(form)

    def get_initial(self):
	self.initial = super(CustomerCompanyUpdateView, self).get_initial()
	self.initial['ateco_sector'] = self.object.ateco_sector.name
	self.initial['cpi'] = self.object.cpi.name
	return self.initial

class CustomerCompanyDeleteView(DeleteView):
    model = CustomerCompany
    form_class = CustomerCompanyForm
    success_url = '/customers/'

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
	self.staff.company = get_object_or_404(CustomerCompany, id=self.kwargs['company'])
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
	self.success_url = reverse('set-working-env', args=[self.kwargs['pk']])
	return super(WorkingEnvironmentEditView, self).form_valid(form)

class DepartmentCreateView(CreateView):
    form_class = DepartmentForm
    template_name = 'customers/department_create_form.html'

    def form_valid(self, form):
	self.department = form.save(commit=False)
	self.department.record_by = self.request.user.get_profile()
	self.department.company = get_object_or_404(CustomerCompany, id=self.kwargs['company'])
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
	self.success_url = reverse('department-detail', args=self.kwargs['company'])
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
	self.companysecurityduty.company = get_object_or_404(CustomerCompany,
							     id=self.kwargs['company'])
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
