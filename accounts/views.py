from django.db.models import F
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .forms import SignupForm, LoginForm
from django.contrib.auth import authenticate, login

def signup(request):
    username = 'AlienX'

    if request.method == 'POST':
        MySignupForm = SignupForm(request.POST)
        if MySignupForm.is_valid():
            username = MySignupForm.cleaned_data['username']
            MySignupForm.save()
            return redirect('login')
            # return render(redirect(('home')))
    else:
        MySignupForm = SignupForm()

    return render(request, 'accounts/signup.html', {
        'form': MySignupForm, 'username': username
    })


def login(request):
    if request.method == 'POST':
        MyLoginForm = LoginForm(request.POST)
        if MyLoginForm.is_valid():
            username = MyLoginForm.cleaned_data['username']
            password = MyLoginForm.cleaned_data['passsword']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                redirect('home')
            else:
                pass
    else:
        MyLoginForm = LoginForm()
    return render(request, 'accounts/login.html', {
        'form': MyLoginForm
    })

def home(request):
    return render(request, 'accounts/home.html')


class HomePageView(TemplateView):
    template_name = "accounts/home.html"
