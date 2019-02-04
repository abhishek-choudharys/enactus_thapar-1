from django.shortcuts import render
from django.http.response import HttpResponseRedirect
from .forms import EventForm
from django.urls import reverse_lazy
from django.views import generic


class EventView(generic.CreateView):
    form_class=EventForm
    success_url=reverse_lazy('index')
    template_name = 'eventform.html'