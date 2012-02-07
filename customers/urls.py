from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('customers.views',
                        url(r'^$', 'list'),
                        url(r'^(?P<customer_id>\d+)/$', 'customer_detail'),
                        url(r'^staff/(?P<staff_id>\d+)/$', 'staff_detail'),
                        )
