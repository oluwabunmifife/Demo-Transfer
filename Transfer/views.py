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

User = get_user_model()

def homeview(request):
    return render(request, "landing_page.html", {})



def registerview(request):
    form = ClientForm
    if form.is_valid():
        first_name = form.cleaned_data['first_name']
        last_name = form.cleaned_data['last_name']
        email = form.cleaned_data['email']
        username = form.cleaned_data['username']
        pin = form.cleaned_data['pin']

        


        #generate account number... Courtesy Jmoraks... Partially
        def genAcc():
            optional_value = string.digits
            result_value = random.sample(optional_value, 10)
            Acc_Num = "".join(result_value)

            if Client.objects.filter(Acc_Num=Acc_Num).exists():
                messages.info(request, "Account Number Already exist")
                genAcc
            else:
                new_client =Client.objects.create(first_name=first_name, last_name=last_name, 
                email=email, username=username, pin=pin, Acc_Num=Acc_Num)
                new_client.save()
                subject = 'WELCOME TO TRANSFER WORLD'
                message = f'Hi {new_client.username}, thank you for registering with us😊. Your Account Number is ' + Acc_Num + ' Cheers!!'
                email_from = settings.EMAIL_HOST_USER
                recipient_list = [new_client.email, ]
                send_mail( subject, message, email_from, recipient_list )

                return redirect("transfer:login")
    else:
        return render(request, "transfer/register.html")

            


    # if request.method == "POST":
    #     first_name = data.cleaned['first_name']
    #     last_name = request.POST['last_name']
    #     email = request.POST['email']
    #     username = request.POST['username']
    #     pin = request.POST['pin']


def login_view(request):
    form = LoginForm
    if form.is_valid():
        username = form.cleaned_data['username']
        pin = form.cleaned_data['pin']
    # if request.method == "POST":
    #     username = request.POST['username']
    #     pin = request.POST['pin']

        user = authenticate(username=username, pin=pin)

        if user is not None:
            login(request, user)
            return redirect('transfer:Home')
        else:
            messages.info(request, 'Invalid username/pin')
            return redirect('transfer:Login')

    else:
        return render(request, "transfer/login.html")

def logout_view(request):
    logout(request)
    return redirect("/")