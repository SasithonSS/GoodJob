from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from users.models import JobberUser


class JobberForm(ModelForm):
    class Meta:
        model = JobberUser
        fields = ['user', 'name', 'gender', 'email', 'phone', 'address', 'province','picture']


class CreateUserForm(UserCreationForm):

    class Meta:
        model = User
        fields =['username', 'email','first_name', 'password1', 'password2']
        



