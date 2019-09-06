from django.views.generic import TemplateView
# from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
# @login_required()


class HomePageView(LoginRequiredMixin, TemplateView):
    template_name = "feeds/home.html"
    login_url = "user:login"
