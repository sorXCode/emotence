from django.contrib.auth import views as auth_view
from django.urls import include, path

from .views import (Login, LoginForm, Logout,
                    ProfileListView, home, login, SignUp, ImageUpdateView
                    )
app_name = "user"
urlpatterns = [
    path('signup/', SignUp.as_view(), name='signup'),
    path('home/', home, name='home'),
    path("login/", Login.as_view(), name="login"),
    path('logout/', Logout.as_view(), name='logout'),
    path('user/<username>/', ProfileListView.as_view(), name='user_profile'),
    path("user/<username>/update", ImageUpdateView.as_view(), name="update"),
]
