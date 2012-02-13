# Create your views here.
from django.views.generic import DetailView
from django.views.generic import ListView
from django.views.generic import YearArchiveView
from django.views.generic import CreateView
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
    model=CustomerCompany
    context_object_name = 'company'

class StaffDetailView(DetailView):
    model=Staff
    context_object_name = 'staff'

class CustomerCompanyCreateView(CreateView):
    form_class = CustomerCompanyForm
    template_name = 'customers/customercompany_create_form.html'
    success_url = '/customers/'

class StaffCreateView(CreateView):
    form_class = StaffForm
    template_name = 'customers/staff_create_form.html'
    success_url = '/customers/'
