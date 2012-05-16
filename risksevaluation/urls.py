from django.conf.urls.defaults import patterns, include, url
from django.contrib.auth.decorators import login_required, permission_required
from django.views.decorators.csrf import csrf_exempt

from risksevaluation.views import RisksEvaluationDocumentDetailView
from risksevaluation.views import RisksEvaluationDocumentCreateView
from risksevaluation.views import RisksEvaluationDocumentUpdateView
from risksevaluation.views import RisksEvaluationDocumentDeleteView
from risksevaluation.views import RisksEvaluationDocumentListView
from risksevaluation.views import AllRisksEvaluationDocumentView
from risksevaluation.views import RiskFactorEvaluationView
from risksevaluation.views import EvalRiskFactorStatusView
from risksevaluation.views import EvalRiskFactorProbabilityView, EvalRiskFactorSeriousnessView
from risksevaluation.views import UntakeMeasureView, TakeMeasureView
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
                           login_required(RiskFactorEvaluationView.as_view()),
                           name = 'eval'),

                       url(r'^(?P<company>\d+)/revision/(?P<revision>\d+)/status$',
                           login_required(csrf_exempt(EvalRiskFactorStatusView.as_view())),
                           name = 'status'),

                       url(r'^(?P<company>\d+)/revision/(?P<revision>\d+)/probeval$',
                           login_required(csrf_exempt(EvalRiskFactorProbabilityView.as_view())),
                           name = 'eval-probability'),

                       url(r'^(?P<company>\d+)/revision/(?P<revision>\d+)/sereval$',
                           login_required(csrf_exempt(EvalRiskFactorSeriousnessView.as_view())),
                           name = 'eval-seriousness'),

                       url(r'^(?P<company>\d+)/revision/(?P<revision>\d+)/take$',
                           login_required(csrf_exempt(TakeMeasureView.as_view())),
                           name = 'take'),

                       url(r'^(?P<company>\d+)/revision/(?P<revision>\d+)/untake$',
                           login_required(csrf_exempt(UntakeMeasureView.as_view())),
                           name = 'untake'),
                       )
