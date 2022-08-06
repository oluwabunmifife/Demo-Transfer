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


def genAcc(first_name, last_name, username, email, pin, request):
    optional_value = string.digits
    result_value = random.sample(optional_value, 10)
    Acc_Num = "".join(result_value)

    if Client.objects.filter(Acc_Num=Acc_Num).exists():
        messages.info(request, "Account Number Already exist")
    else:
        new_client =Client.objects.create(first_name=first_name, last_name=last_name, 
        email=email, username=username, pin=pin, Acc_Num=Acc_Num)
        new_client.save()
        # subject = 'WELCOME TO TRANSFER WORLD'
        # message = f'Hi {new_client.username}, thank you for registering with us😊. Your Account Number is ' + Acc_Num + ' Cheers!!'
        # email_from = settings.EMAIL_HOST_USER
        # recipient_list = [new_client.email, ]
        # send_mail( subject, message, email_from, recipient_list )
        # messages.info(request, "Account Number is " + Acc_Num)