from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    # Examples:
        url(r'^chlst/$', 'checklists.views.index'),
    # url(r'^$', 'secuchecklist.views.home', name='home'),
    # url(r'^secuchecklist/', include('secuchecklist.foo.urls')),
#    url(r'^customers/', include('customers.urls')),
     url(r'^customers/$', 'customers.views.list'),
     url(r'^customers/(?P<customer_id>\d+)/$', 'customers.views.customer_detail'),
     url(r'^customers/staff/(?P<staff_id>\d+)/$', 'customers.views.staff_detail'),
    
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    # Uncomment the next line to enable the admin:
        url(r'^admin/', include(admin.site.urls)),
                       
)
