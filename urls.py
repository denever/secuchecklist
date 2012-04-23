from django.conf.urls.defaults import patterns, include, url

# using django-autocomplete default view
from autocomplete.views import autocomplete
import customers.autocomplete_settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^customers/', include('customers.urls')),
    url(r'^accounts/', include('accounts.urls')),
    url(r'^riskfactors/', include('riskfactors.urls')),
    url(r'^risksevaluation/', include('risksevaluation.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^autocomplete/', include(autocomplete.urls)),
)
