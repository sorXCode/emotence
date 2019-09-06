from django.db.models import F
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .forms import SignupForm, LoginForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView, LogoutView

from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib import messages
from django.db import IntegrityError

class RegisterationView(CreateView):
    template_name = 'user/signup.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('feeds:home')

def signup(request):
    username = 'AlienX'

    if request.method == 'POST':
        MySignupForm = SignupForm(request.POST)
        if MySignupForm.is_valid():
            # username = MySignupForm.cleaned_data['raw_username'].lower()
            # try:
            user = MySignupForm.save(commit=False)
            user.set_password(MySignupForm.cleaned_data['password'])
            user.username = MySignupForm.cleaned_data['raw_username'].lower()
            user.save()
            return redirect('feeds:home')
            # except IntegrityError:
            #     messages.info(request,' Try again, Username Taken')
            # return render(redirect(('home')))
    else:
        MySignupForm = SignupForm()

    return render(request, 'user/base.html', {
        'form': MySignupForm, 'username': username
    })


# def login(request):
#     if request.method == 'POST':
#         MyLoginForm = LoginForm(request.POST)
#         if MyLoginForm.is_valid():
#             username = MyLoginForm.cleaned_data['username']
#             password = MyLoginForm.cleaned_data['password']
#             print(username)
#             user = authenticate(request, username=username, password=password)
#             if user is not None:
#                 login(request, user)
#                 print('logging_in')
#                 redirect('feeds:home')
#     else:
#         MyLoginForm = LoginForm()
#     return render(request, 'user/login.html', {
#         'form': MyLoginForm
#     })


class Login(LoginView):
    form_class = LoginForm
    template_name = 'user/base.html'


class Logout(LogoutView):
    template_name = 'user/logout.html'

def home(request):
    return render(request, 'user/home.html')


# class HomePageView(TemplateView):
#     template_name = "user/home.html"
