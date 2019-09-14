from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.db import IntegrityError
from django.db.models import F
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse_lazy
from django.utils.translation import ugettext_lazy as _
from django.views.generic import CreateView, DetailView, TemplateView, ListView, UpdateView

from .forms import LoginForm, ProfileForm, SignupForm, UserForm
from .models import Profile

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.models import User
from django.views import View


class RegisterationView(CreateView):
    template_name = 'user/signup.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('feeds:home')


class SignUp(View):
    form_class = SignupForm
    template_name = 'user/signup.html'
    username = 'AlienX'

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            fields = ['username', 'email', 'password', 'phone']
            self.username, email, password, phone = [
                form.cleaned_data[field] for field in fields]

            user = User.objects.create_user(
                username=self.username.lower(),
                email=email,
                password=password)
            profile = user.profile
            profile.phone = phone
            profile.raw_username = self.username
            profile.save()
            messages.success(request, _("Signup Successful!"))
            # auth(request, user=user)
            return redirect('feeds:home')
        return render(request, self.template_name, {'form': form})

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name,
                      {
                          'username': self.username,
                          'form': form,
                      })


class Login(LoginView):
    form_class = LoginForm
    template_name = 'user/login.html'


class Logout(LogoutView):
    template_name = 'user/logout.html'


def home(request):
    return render(request, 'user/home.html')




class ProfileView(DetailView):
    queryset = Profile.objects.all().select_related('user')
    template_name = "user/profile.html"
    context_object_name = 'profile_object'


@method_decorator(login_required, name='dispatch')
class ProfileListView(ListView):
    # model = User
    template_name = "user/profile.html"
    context_object_name = 'profile_object'

    def get_queryset(self):
        self.user = get_object_or_404(User,
                                      username=self.kwargs['username'].lower())
        return Profile.objects.filter(user=self.user)
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context["profile_pic_form"] = self.profile_pic_form()
    #     # if self.request.user.is_authenticatd:
    #     #     ProfilePicUpdateForm
    #     return context

    # def profile_pic_form(self):
    #     if self.request.user.is_authenticated:
    #         return ProfilePicUpdateForm
    #     return None


class UserUpdateView(UpdateView):
    model = User
    template_name = "user/update.html"