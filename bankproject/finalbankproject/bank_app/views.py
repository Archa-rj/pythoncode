from django.shortcuts import render
from .models import FinancialService


# Create your views here.

def index(request):
    finance=FinancialService.objects.all()

    return render(request,'index.html',{'finance':finance})