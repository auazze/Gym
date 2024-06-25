from django import forms
from django.contrib.auth.models import User

from .models import Client


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'email']


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['phone_number', 'address', 'date_of_birth']
