from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('username','name','email','position','details','picture','number')

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model=CustomUser
        fields = ('username','email','position','name','details','picture','number')

