from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import Client
from django.contrib.auth import get_user_model
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User, auth
from .forms import ClientForm, LoginForm
from django.contrib import messages
import random #Courtesy Jmoraks
import string #Courtesy Jmoraks
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth.views import LoginView



# Create your views here.

User = get_user_model()

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
        password = request.POST['password']
        Acc_Num = random.randint(100000000, 9999999999)

        if Client.objects.filter(username=username).exists():
            messages.info(request, "Username already exists")
            return redirect("transfer:Register")
        
        elif Client.objects.filter(email=email).exists():
            messages.info(request, "Email already exists")
            return redirect("transfer:Register")

        elif Client.objects.filter(Acc_Num=Acc_Num).exists():
            messages.info(request, "Account number already exists")
            return redirect("transfer:Register")

        else:
            user = Client.objects.create(first_name=first_name, last_name=last_name, email=email, username=username, password=password, Acc_Num=Acc_Num)
            user.save()
        return redirect("transfer:Login")
    else:
        form = ClientForm
        return render(request, "Transfer/register.html", {"form": form})

class ClientLoginView(LoginView):
    template_name = "Transfer/login.html"
    
    def get_success_url(self):
        return "/dashboard"

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(self.request, user)
            return redirect("/dashboard")
        else:
            return redirect("/login")


# def login_view(request):
#     form = LoginForm
#     if request.method == "POST":
#         form = LoginForm(request.POST)
#         username = request.POST['username']
#         password = request.POST['password']
        
#         user = auth.authenticate(username=username, password=password)

#         if user is not None:

#             login(request, user)
#             return redirect("transfer:Dashboard")
#         else:
#             messages.info(request, 'Invalid username/pin')
#             return redirect('transfer:Login')
#     else:
#         return render(request, "Transfer/login.html", {"form": form})



def profile(request, slug):
    user = Client.objects.get(slug=slug)
    return render(request, "profile.html", {"user": user})

def logout_view(request):
    auth.logout(request)
    return redirect("/")




