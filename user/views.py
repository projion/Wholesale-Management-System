from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .form import userRegistration
# Create your views here.
# def login(request):
#     return render(request,"user/login.html")

def signup(request):
    if request.method == "POST":
        reg_form= userRegistration(request.POST)
        if reg_form.is_valid():
            reg_form.save()
            return redirect('user-about')
    else:
        reg_form = userRegistration()
    context= {
            'form' : reg_form
        }
    return render(request,'user/signup.html', context)

def basePage(request):
    return render(request,"user/base.html")