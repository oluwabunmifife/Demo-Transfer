from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import Client
from django.contrib.auth import get_user_model
from django.contrib.auth import login, logout, authenticate
from .forms import ClientForm, LoginForm
from django.contrib import messages
import random #Courtesy Jmoraks
import string #Courtesy Jmoraks
from django.conf import settings
from django.core.mail import send_mail



# Create your views here.

# User = get_user_model()

def homeview(request):
    return render(request, "landing_page.html", {})

def dashboard(request):
    return render(request, "dashboard.html", {})

def registerview(request):
    form = ClientForm
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        username = request.POST['username']
        pin = request.POST['pin']
        Acc_Num = random.randint(100000000, 9999999999)

        if Client.objects.filter(username=username).exists():
            messages.info(request, "Username already exists")
            return redirect("transfer:Register")
        
        elif Client.objects.filter(email=email).exists():
            messages.info(request, "Email already exists")
            return redirect("transfer:Register")

        else:
            form = Client.objects.create(first_name=first_name, last_name=last_name, email=email, username=username, pin=pin, Acc_Num=Acc_Num)
            form.save()
        return redirect("transfer:Login")
    else:
        return render(request, "Transfer/register.html", {"form": form})


def login_view(request):
    form = LoginForm
    if request.method == "POST":
        username = request.POST['username']
        pin = request.POST['pin']
        
        user = authenticate(username=username, pin=pin)

        if user is not None:

            login(request, user)
            return redirect("transfer:Dashboard")
        else:
            messages.info(request, 'Invalid username/pin')
            return redirect('transfer:Login')
    else:
        return render(request, "Transfer/login.html", {"form": form})

def logout_view(request):
    logout(request)
    return redirect("/")




