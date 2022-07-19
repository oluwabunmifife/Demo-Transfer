from django.db import models
# from django.contrib.auth.models import AbstractUser

# Create your models here.

class Client(models.Model):
    # valid_user = models.ForeignKey("Client", on_delete=models.CASCADE)
    first_name = models.CharField("First Name", max_length=35)
    last_name = models.CharField("Last Name", max_length=35)
    email = models.EmailField()
    username = models.CharField("Username", max_length=35)
    Acc_Num = models.CharField("Account Number", max_length=10)
    pin = models.CharField(max_length=4)

    def __str__(self):
        return self.first_name

# class Account(models.Model):
# )
