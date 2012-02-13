from django.conf.urls.defaults import patterns, include, url
from django.contrib.auth.decorators import login_required, permission_required
from customers.models import CustomerCompany, Staff
from customers.views import CustomerCompanyYearView
from customers.views import CustomerCompanyListView
from customers.views import CustomerCompanyDetailView
from customers.views import StaffDetailView
from customers.views import CustomerCompanyCreateView
from customers.views import StaffCreateView
from customers.views import CustomerCompanyUpdateView
from customers.views import StaffUpdateView
from customers.views import CustomerCompanyDeleteView
from customers.views import StaffDeleteView

urlpatterns = patterns('customers.views',
                       url(r'^$', login_required(CustomerCompanyListView.as_view())),
                       url(r'^(?P<pk>\d+)/$', login_required(CustomerCompanyDetailView.as_view())),
                       url(r'^staff/(?P<pk>\d+)/$', login_required(StaffDetailView.as_view())),
                       url(r'year/(?P<year>\d{4})/$', login_required(CustomerCompanyYearView.as_view())),
                       url(r'^create/$', login_required(CustomerCompanyCreateView.as_view())),
                       url(r'^create_staff/$', login_required(StaffCreateView.as_view())),
                       url(r'^update/(?P<pk>\d+)/$', login_required(CustomerCompanyUpdateView.as_view())),
                       url(r'^update_staff/(?P<pk>\d+)/$', login_required(StaffUpdateView.as_view())),
                       url(r'^delete/(?P<pk>\d+)/$', login_required(CustomerCompanyDeleteView.as_view())),
                       url(r'^delete_staff/(?P<pk>\d+)/$', login_required(StaffDeleteView.as_view())),
                       url(r'^(?P<company>\d+)/add_staff/$', login_required(StaffCreateView.as_view())),
                       )
