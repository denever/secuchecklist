# Create your views here.
from django.shortcuts import get_object_or_404
from django.core.urlresolvers import reverse
from django.views.generic import DetailView
from django.views.generic import ListView
from django.views.generic import YearArchiveView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView
from customers.models import *
from customers.forms import CustomerCompanyForm
from customers.forms import StaffForm
from customers.forms import WorkingEnvironmentForm
from customers.forms import DepartmentForm

class CustomerCompanyYearView(YearArchiveView):
    queryset = CustomerCompany.objects.all()
    date_field = 'record_date'
    make_object_list = True

class CustomerCompanyListView(ListView):
    queryset = CustomerCompany.objects.all()
    context_object_name = 'companies'

class CustomerCompanyDetailView(DetailView):
    model = CustomerCompany
    context_object_name = 'company'

class StaffDetailView(DetailView):
    model = Staff
    context_object_name = 'staff'

class CustomerCompanyCreateView(CreateView):
    form_class = CustomerCompanyForm
    template_name = 'customers/customercompany_create_form.html'
    success_url = '/customers/'

    def form_valid(self, form):
        self.company = form.save(commit=False)
        self.company.record_by = self.request.user.get_profile()
        return super(CustomerCompanyCreateView, self).form_valid(form)

class StaffCreateView(CreateView):
    form_class = StaffForm
    template_name = 'customers/staff_create_form.html'

    # def get_initial(self):
    #     super(StaffCreateView, self).get_initial()
    #     self.initial['company'] = self.kwargs['company']
    #     return self.initial

    def form_valid(self, form):
        self.staff = form.save(commit=False)
        self.staff.record_by = self.request.user.get_profile()
        self.staff.company = get_object_or_404(CustomerCompany, id=self.kwargs['company'])
        self.success_url = reverse('staff-detail', args=self.kwargs['company'])
        return super(StaffCreateView, self).form_valid(form)

class CustomerCompanyUpdateView(UpdateView):
    model = CustomerCompany
    form_class = CustomerCompanyForm
    template_name = 'customers/customercompany_update_form.html'
    success_url = '/customers/'

    def form_valid(self, form):
        self.success_url = reverse('company-detail', args=self.kwargs['pk'])
        return super(CustomerCompanyUpdateView, self).form_valid(form)

class StaffUpdateView(UpdateView):
    model = Staff
    form_class = StaffForm
    template_name = 'customers/staff_update_form.html'
    success_url = '/customers/'

    def form_valid(self, form):
        self.success_url = reverse('staff-detail', args=self.kwargs['company'])
        return super(StaffUpdateView, self).form_valid(form)

class CustomerCompanyDeleteView(DeleteView):
    model = CustomerCompany
    form_class = CustomerCompanyForm
    template_name = 'customers/customercompany_delete_form.html'
    success_url = '/customers/'

class StaffDeleteView(DeleteView):
    model = Staff
    form_class = StaffForm
    template_name = 'customers/staff_delete_form.html'
    success_url = '/customers/'

class WorkingEnvironmentEditView(UpdateView):
    form_class = WorkingEnvironmentForm
    model = CustomerCompany
    template_name = 'customers/workingenvironment_create_form.html'
    success_url = '/customers/'
    context_object_name = 'company'

    def form_valid(self, form):
        self.success_url = reverse('company-detail', args=[self.kwargs['pk']])
        return super(WorkingEnvironmentEditView, self).form_valid(form)

class DepartmentCreateView(CreateView):
    form_class = DepartmentForm
    template_name = 'customers/department_create_form.html'

    def form_valid(self, form):
        self.department = form.save(commit=False)
        self.department.record_by = self.request.user.get_profile()
        self.department.company = get_object_or_404(CustomerCompany, id=self.kwargs['company'])
        self.success_url = reverse('department-detail', args=self.kwargs['company'])
        return super(DepartmentCreateView, self).form_valid(form)

class DepartmentDetailView(DetailView):
    model = Department
    context_object_name = 'department'

class DepartmentUpdateView(UpdateView):
    model = Department
    form_class = DepartmentForm
    template_name = 'customers/department_update_form.html'
    success_url = '/customers/'

    def form_valid(self, form):
        self.success_url = reverse('department-detail', args=self.kwargs['company'])
        return super(DepartmentUpdateView, self).form_valid(form)

class DepartmentDeleteView(DeleteView):
    model = Department
    form_class = DepartmentForm
    template_name = 'customers/department_delete_form.html'
    success_url = '/customers/'
