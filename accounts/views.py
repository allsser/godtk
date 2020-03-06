from django.shortcuts import render,redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm, PasswordChangeForm
from .forms import CustomUserChangeForm
from .forms import CustomUserCreationForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import get_user_model

def login(request):
    if request.user.is_authenticated:
        return redirect('godtk:index')

    if request.method =='POST':
        form = AuthenticationForm(request,request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('godtk:index')
    else:
        form = AuthenticationForm()
    context = {'form':form}
    #return render(request,'accounts/auth_form.html',context)
    return render(request,'accounts/login.html',context)

def logout(request):
    auth_logout(request)
    return redirect('godtk:index')