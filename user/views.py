from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .forms import userRegistration
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .models import User
from django.contrib.auth.hashers import make_password, check_password
# Create your views here.

def signup(request):
    if request.method == "POST":
        reg_form= userRegistration(request.POST)
        if reg_form.is_valid():
            reg_form.save()
            #auto login
            # x= reg_form.cleaned_data
            # print(x)
            username= reg_form.cleaned_data.get('username')
            password= reg_form.cleaned_data.get('password1')
            # print(username)
            new_user= authenticate(username=username, password=password)
            login(request, new_user)


            return redirect('about')
        else:
            return render(request, "user/base.html", {'form' : reg_form})

    else:
        reg_form = userRegistration()
    context= {
            'form' : reg_form
        }
    return render(request,'user/signup.html', context)
#####################################################################
def basePage(request):
    return render(request,"user/base.html")
def basePage2(request):
    return render(request,"user/base2.html")
#####################################################################
@login_required()
def userhome(request):
    return render(request,"user/userhome.html")
#####################################################################
def signup2(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        var= request.POST
        user_name = var.get('user_name')
        email = var.get('email')
        password = var.get('password')
        re_password = var.get('re_password')
        age = var.get('age')
        phone = var.get('phone')
        address = var.get('address')
        type = request.POST.get('type')
        all_value = {
            'email' : email,
            'username' : user_name
        }

        obj = User(firstname=first_name, lastname=last_name, username=user_name, user_email=email, password=password, user_age=age, user_phone=phone, user_address=address, user_type=type)

        # print(first_name)

        # Validation [hash-making]
        error_msg= None
        if password != re_password:
            error_msg= 'Password Not Matched!'
        elif User.objects.filter(user_email=email).exists():
            error_msg= 'Already has registered!'

        if not error_msg:
            obj.password = make_password(obj.password)
            obj.save()
            return redirect('login')
        else:
            outdata={
                'error': error_msg,
                'info': all_value
            }
            return render(request, 'user/signup_manual.html', outdata)

    elif request.method == 'GET':
        return render(request, 'user/signup_manual.html')
#####____________________________________________________________________________
def login2(request):
    if request.method == "POST":
        # print('hello.................')
        email = request.POST.get('email')
        password = request.POST.get('password')
        # print(email)
        # print(password)
        userNow= User.get_user_by_mail(email)
        print('userNow :',userNow)
        error_msg = None
        if userNow != False:
            flag = check_password(password, userNow.password)
            print('hello.................2')
            # print(userNow.user_email)
            print("flag is",flag)
            if flag == True:
                request.session['user_is'] = userNow.id
                request.session['user_email'] = userNow.user_email
                print(userNow.id, userNow.user_email)
                print('hello.................3')
                return redirect('home')
            else:
                print('hello.................4')
                error_msg = 'Email or Password Incorrect'
                return render(request, 'user/login_manual.html', {'error': error_msg})
        else:
            error_msg = 'Email or Password Incorrect'
            print('hello.................5')
            return render(request, 'user/login_manual.html', {'error': error_msg})
    if request.method == "GET":
        print('hello.................6')
        return render(request,'user/login_manual.html')

def logout2(request):
    request.session.clear()
    return redirect('Home')

def profile(request):
    varuser=User.objects.all()
    return render(request,'user/profile.html', { 'varuser' : varuser } )




    return render(request,"user/login_manual.html")