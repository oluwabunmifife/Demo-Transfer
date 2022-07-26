from django.urls import path, include
from . import views

app_name = "Transfer"

urlpatterns = [
    path('', views.homeview, name="Home"),
    path('logout', views.logout_view, name="Logout"),
    path('login', views.login_view, name="Login"),
    path('register', views.registerview, name="Register"),
    path('dashboard', views.dashboard, name="Dashboard"),
]