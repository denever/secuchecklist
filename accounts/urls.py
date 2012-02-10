from django.conf.urls.defaults import patterns, include, url
from accounts.views import ProfileView

urlpatterns = patterns('',
                       (r'^profile/$', ProfileView.as_view(),
                        {'template_name': 'accounts/profile.html'}),
                       (r'^login/$', 'django.contrib.auth.views.login',
                        {'template_name': 'accounts/login.html'}),
                       (r'^logout/$', 'django.contrib.auth.views.logout',
                        {'template_name': 'accounts/logout.html'}),
                       (r'^changepasswd/$', 'django.contrib.auth.views.password_change',
                        {'template_name': 'accounts/password_change_form.html'}),
                       (r'^changedone/$', 'django.contrib.auth.views.password_change_done',
                        {'template_name': 'accounts/password_change_done.html'}),
)
