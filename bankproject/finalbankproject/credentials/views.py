# from django.contrib import auth, messages
# from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render,redirect,get_object_or_404

from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# from .forms import PersonCreationForm
# from .models import Person, Office




from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate
from .forms import LoginForm

@login_required()
def sign_in(request):
    if request.method == 'GET':
        form = LoginForm()
        return render(request, 'login.html', {'form': form})

    elif request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                messages.success(request, f'Hi {username.title()}, welcome back!')
                return redirect('dir_form')

        # form is not valid or user is not authenticated
        messages.error(request, f'Invalid username or password')
        return render(request, 'login.html', {'form': form})


# def login_user(request):
#     if request.method == 'POST':
#
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(username=username, password=password)
#         if user is not None:
#             login(request, user)
#             return redirect('dir_form')
#         else:
#             messages.success(request, 'Invalid Credentials,Try Again...')
#             return redirect('login')
#     else:
#
#       return render(request, 'login.html')

from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from .forms import LoginForm, RegisterForm

def sign_up(request):
    if request.method == 'GET':
        form = RegisterForm()
        return render(request, 'register.html', { 'form': form})
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            messages.success(request, 'You have registered successfully.')
            login(request, user)
            return redirect('login')
        else:
            return render(request, 'register.html', {'form': form})




# def register(request):
#     form=UserCreationForm()
#     if request.method == 'POST':
#
#         form=UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('login')
#     return render(request,'register.html',{'form':form})

        #    if request.method =='POST':
        #       username=request.POST['username']
        # password=request.POST['password']
        # cpassword=request.POST['cpassword']
        # if password == cpassword:
        #     if User.objects.filter(username=username).exists():
        #         messages.info(request,'username taken')
        #         return redirect('register')
        #
        #     else:
        #         user=User.objects.create_user(username=username,password=password)
        #         user.save();
        #         return redirect('login')
        #
        #
        # else:
        #     messages.info(request,'password is not matching')
        #     return redirect('register')
        # return redirect('/')
        #
        #  return render(request,'register.html')


def dir_form(request):

    return render(request,'direct_form.html')

def form(request):

     return render(request, 'new.html')

def logout_user(request):
    logout(request)
    return redirect('/')
def submit(request):
    return render(request,'submit.html')
#
# def person_create_view(request):
#     form=PersonCreationForm()
#     if request.method == 'POST':
#         form=PersonCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('add')
#
#     return render(request, 'new.html',{'form':form})
#
#
# def person_update_view(request,pk):
#     person=get_object_or_404(Person, pk=pk)
#     form=PersonCreationForm(instance=person)
#     if request.method == 'POST':
#         form=PersonCreationForm(request.POST,instance=person)
#         if form.is_valid():
#             form.save()
#             return redirect('person_change',pk=pk)
#     return render(request,'new.html',{'form':form})
#
#
#
# def load_cities(request):
#     district_id=request.GET.get('district_id')
#     office=Office.objects.filter(district_id=district_id).all()
#     return render(request,'dropdown_list.html',{'office':office})

#
#
#
#
#
#
#
#
#
#
#
#
#
#
#









# from django.http import JsonResponse
# from django.shortcuts import render, redirect, get_object_or_404
#
from .forms import PersonCreationForm
from .models import Person, Office


def person_create_view(request):
    form = PersonCreationForm()
    if request.method == 'POST':
        form = PersonCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('person_add')
    return render(request, 'new.html', {'form': form})


def person_update_view(request, pk):
    person = get_object_or_404(Person, pk=pk)
    form = PersonCreationForm(instance=person)
    if request.method == 'POST':
        form = PersonCreationForm(request.POST, instance=person)
        if form.is_valid():
            form.save()
            return redirect('person_change', pk=pk)
    return render(request, 'new.html', {'form': form})


# AJAX
def load_cities(request):
    district_id = request.GET.get('district_id')
    office = Office.objects.filter(district_id=district_id).all()
    return render(request, 'dropdown_list.html', {'office': office})
    # return JsonResponse(list(cities.values('id', 'name')), safe=False)