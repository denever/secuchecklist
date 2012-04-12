from django.conf.urls.defaults import patterns, include, url
from django.contrib.auth.decorators import login_required, permission_required

from riskfactors.views import RiskFactorTreeView
from riskfactors.views import RiskFactorDetailView
from riskfactors.views import RiskFactorCreateView
from riskfactors.views import RiskFactorUpdateView
from riskfactors.views import RiskFactorDeleteView
from riskfactors.views import RiskFactorTreeJson
from riskfactors.views import RiskFactorSubTreeJson

urlpatterns = patterns('riskfactors.views',
                       url(r'^$', login_required(RiskFactorTreeView.as_view()),
                           name='riskfactors'),

                       url(r'^tree/$', login_required(RiskFactorTreeJson.as_view()),
                           name='riskfactors-jsontree'),

                       url(r'^(?P<pk>\d+)/$',
                           login_required(RiskFactorDetailView.as_view()),
                           name = 'riskfactor-detail'),

                       url(r'^(?P<pk>\d+)/subtree/$', login_required(RiskFactorSubTreeJson.as_view()),
                           name='riskfactor-subtree'),

                       url(r'^create/$',
                           login_required(RiskFactorCreateView.as_view()),
                           name = 'riskfactor-create'
                           ),

                       url(r'^(?P<pk>\d+)/update/$',
                           login_required(RiskFactorUpdateView.as_view()),
                           name = 'riskfactor-edit'
                           ),

                       url(r'^delete_riskfactor/(?P<pk>\d+)/$',
                           login_required(RiskFactorDeleteView.as_view()),
                           name = 'riskfactor-delete'
                           ),
                       )
