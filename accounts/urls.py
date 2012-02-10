from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('',
                       # (r'^profile/$', 'django.contrib.auth.views.profile',
                       #  {'template_name': 'accounts/profile.html'}),
                       (r'^login/$', 'django.contrib.auth.views.login',
                        {'template_name': 'accounts/login.html'}),
                       (r'^logout/$', 'django.contrib.auth.views.logout',
                        {'template_name': 'accounts/logout.html'}),
)
