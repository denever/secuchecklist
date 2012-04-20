from django.conf.urls.defaults import patterns, include, url
from django.contrib.auth.decorators import login_required, permission_required

from checklists.views import CheckListDetailView
from checklists.views import CheckListCreateView
from checklists.views import CheckListUpdateView
from checklists.views import CheckListDeleteView
from checklists.views import CheckListListView
from checklists.views import AllCheckListView

urlpatterns = patterns('checklists.views',
                       url(r'^$', login_required(AllCheckListView.as_view()),
                           name='checklists'),

                       url(r'^/company/(?P<pk>\d+)$', login_required(CheckListListView.as_view()),
                           name='checklists-company'),

                       url(r'^(?P<pk>\d+)/$',
                           login_required(CheckListDetailView.as_view()),
                           name = 'checklist-detail'),

                       url(r'^create/$',
                           login_required(CheckListCreateView.as_view()),
                           name = 'checklist-create'
                           ),

                       url(r'^(?P<pk>\d+)/update/$',
                           login_required(CheckListUpdateView.as_view()),
                           name = 'checklist-edit'
                           ),

                       url(r'^delete_checklist/(?P<pk>\d+)/$',
                           login_required(CheckListDeleteView.as_view()),
                           name = 'checklist-delete'
                           ),
                       
                       url(r'^add/(?P<pk>\d+)/$',
                           login_required(CheckListCreateView.as_view()),
                           name = 'checklist-add'
                           ),

                       )
