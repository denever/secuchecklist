from django.conf.urls.defaults import patterns, include, url
from django.contrib.auth.decorators import login_required, permission_required

from risksevaluation.views import RisksEvaluationDocumentDetailView
from risksevaluation.views import RisksEvaluationDocumentCreateView
from risksevaluation.views import RisksEvaluationDocumentUpdateView
from risksevaluation.views import RisksEvaluationDocumentDeleteView
from risksevaluation.views import RisksEvaluationDocumentListView
from risksevaluation.views import AllRisksEvaluationDocumentView
from risksevaluation.views import RiskEvaluationCreateView
#from risksevaluation.views import CheckRiskFactor

# red stands for Risks Evaluation Document

urlpatterns = patterns('risksevaluation.views',
                       url(r'^$', login_required(AllRisksEvaluationDocumentView.as_view()),
                           name='red'),

                       url(r'^company/(?P<company>\d+)$', login_required(RisksEvaluationDocumentListView.as_view()),
                           name='red-list'),

                       url(r'^(?P<company>\d+)/revision/(?P<pk>\d+)/$',
                           login_required(RisksEvaluationDocumentDetailView.as_view()),
                           name = 'red-detail'),

                       url(r'^(?P<company>\d+)/create/$',
                           login_required(RisksEvaluationDocumentCreateView.as_view()),
                           name = 'red-create'
                           ),

                       url(r'^(?P<company>\d+)/edit/(?P<pk>\d+)/$',
                           login_required(RisksEvaluationDocumentUpdateView.as_view()),
                           name = 'red-edit'
                           ),

                       url(r'^(?P<company>\d+)/delete/(?P<pk>\d+)/$',
                           login_required(RisksEvaluationDocumentDeleteView.as_view()),
                           name = 'red-delete'
                           ),
                       url(r'^(?P<company>\d+)/revision/(?P<revision>\d+)/eval/(?P<riskfactor>\d+)/$',
                           login_required(RiskEvaluationCreateView.as_view()),
                           name = 'eval'),
                       # url(r'^check_factor',
                       #     login_required(CheckRiskFactor.as_view()),
                       #     name= 'check')
                       )
