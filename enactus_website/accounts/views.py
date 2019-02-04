from django.shortcuts import render
from django.http.response import HttpResponseRedirect
from .forms import CustomUserCreationForm,CustomUserChangeForm
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import TemplateView
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash

class SignUPView(generic.CreateView):
    form_class=CustomUserCreationForm
    success_url=reverse_lazy('login')
    template_name = 'signup.html'

def EditUser(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = CustomUserChangeForm(instance=request.user)
        args = {'form':form}
        return render(request, 'edit_profile.html', args)

def ChangePassword(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request,form.user)
            return HttpResponseRedirect('/')
    else:
        form = PasswordChangeForm(user=request.user)
        args = {'form':form}
        return render(request, 'password-change.html', args)

