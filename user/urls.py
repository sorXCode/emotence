from django.urls import path, include
from .views import signup, home, login, LoginForm
from .views import Login, Logout

from django.contrib.auth import views as auth_view

app_name = "user"
urlpatterns = [
    path('signup/', signup, name='signup'),
    # path('signup/', RegisterationView.as_view(), name='signup'),
    path('home/', home, name='home'),
    # path("login/", auth_view.LoginView.as_view(), name="login"),
    path("login/", Login.as_view(), name="login"),
    path('logout/', Logout.as_view(), name='logout'),
    # path("login/", login, name="login"),
]
