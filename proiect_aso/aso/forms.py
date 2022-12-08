from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from django import forms
from django.utils.text import slugify
from .models import Room


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']


class RoomForm(ModelForm):
    name = forms.TextInput()
    slug = forms.TextInput()
    class Meta:
        model = Room
        fields = ['name','slug']
