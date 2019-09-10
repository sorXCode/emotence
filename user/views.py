from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.db import IntegrityError
from django.db.models import F
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView, DetailView

from .forms import LoginForm, SignupOthers, SignupEmail, ProfileForm, UserForm
from .models import Profile


class RegisterationView(CreateView):
    template_name = 'user/signup.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('feeds:home')


def signup(request):
    username = 'AlienX'

    if request.method == 'POST':
        MySignupOthers = SignupOthers(request.POST)
        MySignupEmail = SignupEmail(request.POST)
        # MySignupEmail = SignupEmail(request.POST['SignupEmail'])
        if MySignupOthers.is_valid() and MySignupEmail.is_valid():
            # username = MySignupForm.cleaned_data['raw_username'].lower()
            # try:
            user = MySignupEmail.save(commit=False)
            user.set_password(MySignupOthers.cleaned_data['password'])
            user.username = MySignupOthers.cleaned_data['raw_username'].lower()
            user.raw_username = MySignupOthers.cleaned_data['raw_username']
            user.save()
            return redirect('feeds:home')
            # except IntegrityError:
            #     messages.info(request,' Try again, Username Taken')
            # return render(redirect(('home')))
    else:
        MySignupOthers = SignupOthers()
        MySignupEmail = SignupEmail()

    return render(request, 'user/base.html', {
        'form': [MySignupOthers, MySignupEmail], 'username': username
    })




class Login(LoginView):
    form_class = LoginForm
    template_name = 'user/base.html'


class Logout(LogoutView):
    template_name = 'user/logout.html'


def home(request):
    return render(request, 'user/home.html')


class ProfileView(DetailView):
    queryset = Profile.objects.all().select_related('user')
    template_name = "user/profile.html"

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
