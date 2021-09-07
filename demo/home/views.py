from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import SignupForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
# Create your views here.
def signup(request):
    if request.user.is_authenticated:
        return redirect('/main')
    else:
        if request.method == 'POST':
            fm = SignupForm(request.POST)
            if fm.is_valid():
                fm.save()
                messages.success(request,"Your Account is created !!!")
                fm = SignupForm()
        else:
            fm = SignupForm()
        return render(request,'signup.html', {'form':fm})

def done(request):
    if request.user.is_authenticated:
        return render(request, "main.html")
    else:
        return redirect('/')

def login_page(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            fm = AuthenticationForm(request=request, data=request.POST)
            if fm.is_valid():
                uname = fm.cleaned_data['username']
                upass = fm.cleaned_data['password']
                user = authenticate(username=uname, password=upass)
                if user is not None:
                    login(request, user)
                    messages.success(request,"You are logged in successfully!!!!")
                    return redirect('/main')
        else:
            fm = AuthenticationForm()
        return render(request, 'login.html', {'form': fm})
    else:
        return redirect('/main')

def logout_page(request):
    logout(request)
    return redirect('/')
