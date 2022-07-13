from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Client(AbstractUser):
    # valid_user = models.ForeignKey("Client", on_delete=models.CASCADE)
    Acc_Num = models.CharField("Account Number", max_length=10)
    pin = models.CharField(max_length=4)

    # def __str__(self):
    #     return self.F_name, self.L_name

# class Account(models.Model):
# )
