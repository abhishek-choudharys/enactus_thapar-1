from django.shortcuts import render
from django.views.generic import TemplateView


class homepage(TemplateView):
        template_name = 'index.html'
# Create your views here.

class ProfileView(TemplateView):
        template_name = 'profile.html'