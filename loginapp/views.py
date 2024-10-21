from django.shortcuts import render,redirect
from .forms import LoginModelForm
from .models import UserDetails
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.forms import AuthenticationForm
# from django.contrib.auth import login,logout
# from django.contrib.auth.decorators import login_required
# Create your views here.
def registration(request):
 

    if request.method == 'POST':
        form = LoginModelForm(request.POST)
        if form.is_valid():
            db = form.save()
            return render(request, 'submission.html', {
                'message': 'Data Saved to DB',
                'db': db
            })
    else:
        form = LoginModelForm()

    return render(request, 'form.html', {'form': form})

def display(request):

   
    datas=UserDetails.objects.all().values('id','name')
    return render(request,'form-data.html',{'datas':datas})

def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')



# def pagevisit(request):
#     count = request.session.get('page_count',0)
#     count +=1
#     request.session['page_count'] = count
#     return render(request,'page_visit.html' , {'count':count})

# def signup_page(request):
#     if request.method == 'POST':
#         user_form = UserCreationForm(request.POST)
#         if user_form.is_valid():
#             user_form.save()
#             return redirect ('home')
#     else:
#         user_form = UserCreationForm()
#     return render(request,'signup.html',{'user_form':user_form})  


# def login_page(request):
#     if request.method == 'POST':
#         form = AuthenticationForm(data=request.POST)
#         if form.is_valid():
#             user = form.get_user()
#             login(request,user)
#             return redirect ('register')
#     else:
#             form = AuthenticationForm()
#     return render(request,'login.html',{'form':form})    


# @login_required(login_url='/login/')
# def logout_view(request):
#     if request.method == 'POST':
#         logout(request)
#         return redirect('login')
#     context = {
#         'user': request.user
#     }
#     return render(request,'logout.html',context)