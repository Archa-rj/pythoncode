from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
# from .forms import Person,PersonForm
# from .models import City,District
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('form')
        else:
            messages.info(request, 'Invalid Credentials')
            return redirect('login')

    return render(request, 'login.html')
def register(request):
    if request.method=='POST':
        username=request.POST['username']


        password=request.POST['password']
        cpassword=request.POST['cpassword']
        if password==cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,'username taken')
                return redirect('register')

            else:
                user=User.objects.create_user(username=username,password=password)
                user.save();
                return redirect('login')


        else:
            messages.info(request,'password is not matching')
            return redirect('register')
            return redirect('/')
    return render(request,'register.html')

def form(request):

     return render(request, 'new.html')

def logout(request):
    auth.logout(request)
    return redirect('/')
def submit(request):
    return render(request,'submit.html')

























# from django.http import JsonResponse
# from django.shortcuts import render, redirect, get_object_or_404
#
# from .forms import PersonCreationForm
# from .models import Person, City
#
#
# def person_create_view(request):
#     form = PersonCreationForm()
#     if request.method == 'POST':
#         form = PersonCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('person_add')
#     return render(request, 'persons/home.html', {'form': form})
#
#
# def person_update_view(request, pk):
#     person = get_object_or_404(Person, pk=pk)
#     form = PersonCreationForm(instance=person)
#     if request.method == 'POST':
#         form = PersonCreationForm(request.POST, instance=person)
#         if form.is_valid():
#             form.save()
#             return redirect('person_change', pk=pk)
#     return render(request, 'new.html', {'form': form})
#
#
# # AJAX
# def load_cities(request):
#     country_id = request.GET.get('country_id')
#     cities = City.objects.filter(country_id=country_id).all()
#     return render(request, 'dropdown_list_.html', {'cities': cities})
    # return JsonResponse(list(cities.values('id', 'name')), safe=False)