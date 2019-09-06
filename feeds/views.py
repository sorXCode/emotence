from django.views.generic import TemplateView
# from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
# @login_required()

<<<<<<< HEAD

class HomePageView(LoginRequiredMixin, TemplateView):
    template_name = "feeds/home.html"
    login_url = "user:login"
||||||| merged common ancestors
class HomePageView(TemplateView):
    template_name = "home.html"
=======

class HomePageView(TemplateView):
    template_name = "home.html"
>>>>>>> master
