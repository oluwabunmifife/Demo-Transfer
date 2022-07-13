from django import forms
from .models import Client


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client

        fields = [
            "first_name", "last_name", "email", "username", "pin"
        ]

        widget = {
            'pin': forms.PasswordInput(),
        }

class LoginForm(forms.Form):
    class Meta:
        username = forms.CharField(max_length=20)
        password = forms.CharField(max_length=20, widget=forms.PasswordInput)