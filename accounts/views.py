# Create your views here.
from django.shortcuts import get_object_or_404

from django.views.generic import TemplateView
from django.views.generic import ListView, DetailView
from django.utils import simplejson

from accounts.models import UserProfile, Activity

class ProfileView(TemplateView):
    template_name = "accounts/profile.html"

class ActivityListView(ListView):
    context_object_name = 'activities'

    def get_queryset(self):
        user_profile = self.request.user.get_profile()
        return user_profile.activity_set.all().order_by('-date')

class ActivityDetailView(DetailView):
    model = Activity
    context_object_name = 'activity'

    def get_context_data(self, **kwargs):
        context = super(ActivityDetailView, self).get_context_data(**kwargs)
        activity = context['activity']
        try:
            context['diff_list'] = simplejson.loads(activity.serialized_data)
        except Exception, e:
            print e
        return context
