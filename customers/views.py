# Create your views here.
from django.views.generic import DetailView, ListView, YearArchiveView
from customers.models import *

class CustomerCompanyYearView(YearArchiveView):
    queryset = CustomerCompany.objects.all()
    date_field = 'record_date'
    make_object_list = True

class CustomerCompanyListView(ListView):
    queryset = CustomerCompany.objects.all()

class CustomerCompanyDetailView(DetailView):
    model=CustomerCompany
    context_object_name = 'company'

class StaffDetailView(DetailView):
    model=Staff
    context_object_name = 'staff'    
