# Create your views here.
from django.views.generic import DetailView
from django.views.generic import ListView
from django.views.generic import YearArchiveView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView
from customers.models import *
from customers.forms import CustomerCompanyForm
from customers.forms import StaffForm

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
    success_url = '/customers/'

class CustomerCompanyUpdateView(UpdateView):
    model = CustomerCompany
    form_class = CustomerCompanyForm
    template_name = 'customers/customercompany_update_form.html'
    success_url = '/customers/'

class StaffUpdateView(UpdateView):
    model = Staff
    form_class = StaffForm
    template_name = 'customers/staff_update_form.html'
    success_url = '/customers/'

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
