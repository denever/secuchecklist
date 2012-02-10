from django.conf.urls.defaults import patterns, include, url
from customers.models import CustomerCompany, Staff
from customers.views import CustomerCompanyYearView
from customers.views import CustomerCompanyListView
from customers.views import CustomerCompanyDetailView
from customers.views import StaffDetailView
from django.views.generic import DetailView, ListView

urlpatterns = patterns('customers.views',
                       url(r'^$', CustomerCompanyListView.as_view()),
                       url(r'^(?P<pk>\d+)/$', CustomerCompanyDetailView.as_view()),
                       url(r'^staff/(?P<pk>\d+)/$', StaffDetailView.as_view()),
                       url(r'year/(?P<year>\d{4})/$', CustomerCompanyYearView.as_view()),
                       )
