from django.urls import path, include
from . import views
from django.contrib.auth.views import LoginView
from .views import ClientLoginView

app_name = "Transfer"

urlpatterns = [
    path('', views.homeview, name="Home"),
    path('logout', views.logout_view, name="Logout"),
    path('login', ClientLoginView.as_view(), name="Login"),
    path('register', views.registerview, name="Register"),
    path('dashboard', views.dashboard, name="Dashboard"),
    path('profile/<slug:slug>/', views.profile, name="Profile")
]