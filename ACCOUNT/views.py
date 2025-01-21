from django.shortcuts import render, redirect
from.forms import LoginForm, userRegisterForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import logout, login, authenticate
from django.contrib import auth
from BLOOD.models import Blood
from BLOOD.forms import RecipientForm


def userregister(request):
    forms=userRegisterForm()
    
    if request.method=="POST":
        forms=userRegisterForm(request.POST)
        if forms.is_valid():
            forms.save()
            messages.success(request, 'successfull account created')
            return redirect('login')
        
        else:
            messages.error(request, 'Error in creating account')
            return redirect('register')
        
    context={
        'form':forms
    }
    return render(request, 'user/register.html', context)


def userlogin(request):
    forms=LoginForm()
    if request.method =="POST":
        username=request.POST.get('name')
        psw=request.POST.get('password')
        
        user=authenticate(request,username=username, password=psw)
        if user is not None:
            login(request, user)
            messages.success(request, "Success Login")
            return redirect('dashboard')
        else:
            messages.error(request, 'user not have account please create!!!!!!')
            return redirect('login')
    context={
        "form":forms
    }
    return render(request, 'user/login.html', context)

def logout(request):
    auth.logout(request)
    return redirect("login")





