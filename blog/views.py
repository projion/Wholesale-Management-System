from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.

def homepage(request):
    return render(request,"blog/homepage.html")
def aboutPage(request):
    return render(request,"blog/about.html")
@login_required
def contactPage(request):
    return render(request,"blog/contact.html")