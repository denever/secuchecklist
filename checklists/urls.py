from django.conf.urls.defaults import patterns, include, url
from django.contrib.auth.decorators import login_required, permission_required

from checklists.views import ChecklistDetailView
from checklists.views import ChecklistCreateView
from checklists.views import ChecklistUpdateView
from checklists.views import ChecklistDeleteView
from checklists.views import ChecklistListView
from checklists.views import AllChecklistView

urlpatterns = patterns('checklists.views',
                       url(r'^$', login_required(AllChecklistView.as_view()),
                           name='checklists'),

                       url(r'^company/(?P<company>\d+)$', login_required(ChecklistListView.as_view()),
                           name='checklists-list'),

                       url(r'^(?P<company>\d+)/(?P<pk>\d+)/$',
                           login_required(ChecklistDetailView.as_view()),
                           name = 'checklist-detail'),

                       url(r'^create/(?P<company>\d+)/$',
                           login_required(ChecklistCreateView.as_view()),
                           name = 'checklist-create'
                           ),

                       url(r'^(?P<company>\d+)/edit/(?P<pk>\d+)/$',
                           login_required(ChecklistUpdateView.as_view()),
                           name = 'checklist-edit'
                           ),

                       url(r'^(?P<company>\d+)/delete/(?P<pk>\d+)/$',
                           login_required(ChecklistDeleteView.as_view()),
                           name = 'checklist-delete'
                           ),
                       )
