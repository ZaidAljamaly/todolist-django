from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import Task
from django.contrib.auth.forms import UserCreationForm
from django import forms


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = '__all__'
        exclude = ['user', 'complete']


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
