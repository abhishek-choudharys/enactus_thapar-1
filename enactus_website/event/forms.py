from django import forms
from django.forms import ModelForm
from .models import Events

class EventForm(ModelForm):
    class Meta:
        model=Events
        fields=['name','email','branch','Year','Rollno','event']

