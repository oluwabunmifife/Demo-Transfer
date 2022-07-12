from django.db import models
from django.contrib.auth import User
# Create your models here.

class Client(models.Model):
    F_name = models.CharField(max_length=35)
    L_name = models.CharField(max_length=35)
    Acc_Num = models.IntegerField(models.OneToOneField("Account.Model", on_delete=models.CASCADE))
    pin = models.IntegerField()

    def __str__(self):
        return self.F_name, self.L_name
