from django.shortcuts import render
from .forms import FeedBackFromUser
from django.contrib.auth.decorators import login_required

# Create your views here.
def contact(request):
    return render(request,'contact.html')

# def contact_us(request):
#     if request.method == 'GET':
#         form = FeedBackFromUser(request.GET)
#         if form.is_valid():
#             db=form.save()
#             return render(request,'regards.html',{
#                 db:'db'
#             })
#     else:
#         form=FeedBackFromUser()
#         return render (request,'contactus.html',{'form':form})

@login_required(login_url='/login/')
def contact_us(request):
    if request.method == 'GET':
        form = FeedBackFromUser(request.GET)
        if form.is_valid():
            db = form.save()
            return render(request, 'regards.html', {'db': db})  # Corrected the dictionary key-value pair
        else:
            return render(request, 'contactus.html', {'form': form})  # Handle invalid form submission
    else:
        form = FeedBackFromUser()
        return render(request, 'contactus.html', {'form': form})

