# from django.contrib import admin
from django.urls import path, include
from . import views


app_name = 'feeds'
urlpatterns = [
    path("", views.HomePageView.as_view(), name="home"),
    path("accounts/", include('django.contrib.auth.urls')),
    path('accounts/', include('accounts.urls')),
]
