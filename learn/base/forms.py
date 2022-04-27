from dataclasses import field
from django.forms import ModelForm
from django import forms
from .models import Room
from django.contrib.auth.models import User
from django.contrib.auth.forms  import UserCreationForm 


class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = '__all__'
        exclude = ['host', 'participants']

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']




class registerForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email',  'password1', 'password2']