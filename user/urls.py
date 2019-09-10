from django.contrib.auth import views as auth_view
from django.urls import include, path

from .views import Login, LoginForm, Logout, ProfileView, home, login, signup

app_name = "user"
urlpatterns = [
    path('signup/', signup, name='signup'),
    # path('signup/', RegisterationView.as_view(), name='signup'),
    path('home/', home, name='home'),
    # path("login/", auth_view.LoginView.as_view(), name="login"),
    path("login/", Login.as_view(), name="login"),
    path('logout/', Logout.as_view(), name='logout'),
    path('<str:username>/', ProfileView.as_view(), name='user_profile')
    # path("login/", login, name="login"),
]
