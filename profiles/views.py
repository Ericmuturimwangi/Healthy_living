from django.views.generic import TemplateView
from .models import Profile
from django.shortcuts import get_object_or_404


class Profiles(TemplateView):
    template_name = "profiles/profile.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Fetch the profile or return a 404 page if not found
        context["profile"] = get_object_or_404(Profile, slug=self.kwargs["pk"])
        return context
