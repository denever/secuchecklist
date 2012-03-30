# Create your views here.
from django.shortcuts import get_object_or_404

from django.views.generic import TemplateView
from django.views.generic import ListView

from accounts.models import UserProfile

class ProfileView(TemplateView):
    template_name = "accounts/profile.html"

class ActivityListView(ListView):
    context_object_name = 'activities'

    def get_queryset(self):
        user_profile = self.request.user.get_profile()
        return user_profile.activity_set.all().order_by('-date')
