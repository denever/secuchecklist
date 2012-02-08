from django.conf.urls.defaults import patterns, include, url
from django.views.generic import DetailView, ListView
from customers.models import CustomerCompany, Staff

urlpatterns = patterns('customers.views',
                       url(r'^$', ListView.as_view(queryset=CustomerCompany.objects.all(),
                                                   context_object_name='cc_list')),
                       url(r'^(?P<pk>\d+)/$', DetailView.as_view(model=CustomerCompany,
                                                                 context_object_name='company')),
                       url(r'^staff/(?P<pk>\d+)/$', DetailView.as_view(model=Staff,
                                                                 context_object_name='staff')),
                       )

#                        url(r'^$', 'list'),
#                        url(r'^(?P<customer_id>\d+)/$', 'customer_detail'),
#                        url(r'^staff/(?P<staff_id>\d+)/$', 'staff_detail'),
