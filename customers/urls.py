from django.conf.urls.defaults import patterns, include, url
from django.contrib.auth.decorators import login_required, permission_required
from customers.models import CustomerCompany, Staff
from customers.views import CustomerCompanyYearView
from customers.views import CustomerCompanyListView
from customers.views import CustomerCompanyDetailView
from customers.views import StaffDetailView
from customers.views import CustomerCompanyCreateView
from customers.views import StaffCreateView

urlpatterns = patterns('customers.views',
                       url(r'^$', login_required(CustomerCompanyListView.as_view())),
                       url(r'^(?P<pk>\d+)/$', login_required(CustomerCompanyDetailView.as_view())),
                       url(r'^staff/(?P<pk>\d+)/$', login_required(StaffDetailView.as_view())),
                       url(r'year/(?P<year>\d{4})/$', login_required(CustomerCompanyYearView.as_view())),
                       url(r'^create/$', login_required(CustomerCompanyCreateView.as_view())),
                       url(r'^create_staff/$', login_required(StaffCreateView.as_view())),                       
                       )
