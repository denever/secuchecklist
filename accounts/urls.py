from django.contrib.auth.decorators import login_required, permission_required
from django.conf.urls.defaults import patterns, include, url
from accounts.views import ProfileView, ActivityListView

urlpatterns = patterns('accounts.views',
                       url(r'^profile/$',
                           login_required(ProfileView.as_view()),
                           name='profile'
                           ),

                       url(r'^activity/$',
                           login_required(ActivityListView.as_view()),
                           name='activity'),
                       )

urlpatterns += patterns('',
                       (r'^login/$', 'django.contrib.auth.views.login',
                        {'template_name': 'accounts/login.html'},
                        "login"
                        ),

                       (r'^logout/$', 'django.contrib.auth.views.logout',
                        {'template_name': 'accounts/logout.html'},
                        "logout",
                        ),

                       (r'^changepasswd/$', 'django.contrib.auth.views.password_change',
                        {'template_name': 'accounts/password_change_form.html'},
                        'change-passwd',
                        ),

                       (r'^changedone/$', 'django.contrib.auth.views.password_change_done',
                        {'template_name': 'accounts/password_change_done.html'},
                        ),
                        )
