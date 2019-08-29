from django.urls import path, include
from .views import login, signup, home


urlpatterns = [
    path('signup/', signup, name='signup'),
    path('home/', home, name='home'),
    path("login/", login, name="login"),
]
