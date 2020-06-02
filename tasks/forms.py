from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email','password1','password2']

class TaskForm(forms.ModelForm):
    class Meta:
        model=Task
        fields="__all__"