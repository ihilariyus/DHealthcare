from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.decorators import login_required
from app.forms import RegistrationForm 


def LoginView(request):
    return render(request,'login.html')


def signup(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')

    else:
        form=RegistrationForm()
    context = {
        'form':form
    }    
    return render(request,'signup.html',context)

@login_required
def Dashboard(request):
    return render(request,'UserDashboard.html')

    

def userdashboard(request):
    return render(request,'dashBoard.html')


def doclogin(request):  
    username = 'admin'
    password = 'admin'
    if request.method == "POST":
        name_gn = request.POST['username']
        password_gn = request. POST['password']
        if username==name_gn and password==password_gn:
            return redirect('userdashboard')
        else:
            context = {'error: "wrong'}
        
    
    return render(request,'loginUser.html')

