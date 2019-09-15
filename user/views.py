from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.db import IntegrityError
from django.db.models import F
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.utils.translation import ugettext_lazy as _
from django.views import View
from django.views.generic import (CreateView, DetailView, ListView,
                                  TemplateView, UpdateView)

from .forms import LoginForm, ProfileForm, SignupForm, ImageForm
from .models import Profile, UserImage


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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["images_form"] = self.profile_image_form()
        return context

    def profile_image_form(self):
        if self.request.user.is_authenticated:
            return ImageForm()

    def get_queryset(self):
        self.user = get_object_or_404(User,
                                      username=self.kwargs['username'].lower())
        self.profile = Profile.objects.filter(user=self.user)
        self.userImage = UserImage.objects.all()
        # print(len(self.userImage))
        print(self.userImage)
        return self.profile


class ProfileUpdateView(View):
    form_class = ProfileForm
    template_name = "user/update.html"

    def get(self, request, *args, **kwargs):
        # if self.request.user.is_authenticated():
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        profile = self.form_class(request.POST)
        if profile.is_valid():
            profile.save()


class ImageUpdateView(View):
    form_class = ImageForm
    template_name = 'user/update.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            print('dkdkd')
            return redirect("user:user_profile", request.user)
        else:
            print("no non non")
            form = self.form_class()

        return render(request, self.template_name, {'form': form})
