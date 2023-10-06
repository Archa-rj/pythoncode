from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.

def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'Invalid Credentials')
            return redirect('login')


    return render(request,'login.html')
def registration(request):
    if request.method=='POST':
        username=request.POST['username']
        firstname=request.POST['firstname']
        name2=request.POST['secondname']
        email=request.POST['email']
        password=request.POST['password']
        cpassword=request.POST['pd']
        if password==cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,'username taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'email  taken')
                return redirect('register')
            else:
                user=User.objects.create_user(username=username,password=password,first_name=firstname,last_name=name2,email=email)
                user.save();
                return redirect('login')


        else:
            messages.info(request,'password is not matching')
            return redirect('register')
            return redirect('/')
    return render(request,'reg.html')

    # return render(request,'reg.html')
def logout(request):
    auth.logout(request)
    return redirect('/')