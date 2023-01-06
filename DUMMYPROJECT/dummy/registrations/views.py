from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect

def login(request):
    if request.method == 'POST':
        user_name = request.POST['user_name']
        pswd=request.POST['pswd']
        user=auth.authenticate(username=user_name, password=pswd)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"Username or Password not matched")
            return redirect('login')

    return render(request,'login.html')



def register(request):
    if request.method == 'POST':
        user_name = request.POST['user_name']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        e_mail = request.POST['e_mail']
        pswd = request.POST['pswd']
        pswd1 = request.POST['pswd1']
        if pswd == pswd1:
            if User.objects.filter(username=user_name).exists():
                messages.info(request,"User name already exists")
                return redirect('register')

            elif User.objects.filter(email=e_mail).exists():
                messages.info(request,"Email already exists")
                return redirect('register')

            else:
                user=User.objects.create_user(username=user_name,first_name=first_name,last_name=last_name,email=e_mail,password=pswd)
                user.save();
                return redirect('login')

        else:
            messages.info(request,"Password not Matched")
            return redirect('register')



    return render(request,'register.html')


def logout(request):
    auth.logout(request)
    return redirect('/')

#import sys
#print(sys.prefix)
