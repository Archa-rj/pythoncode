from django.shortcuts import render, redirect
from .models import Cartoon
from .forms import CartoonForm
# Create your views here.
def index(request):
    cartoon=Cartoon.objects.all()
    return render(request,'index.html',{'cartoon':cartoon})
def detail(request,c_id):
    cartoon=Cartoon.objects.get(id=c_id)
    return render(request,'detail.html',{'cartoon':cartoon})

def add(request):
    if request.method == 'POST':
       name=request.POST.get('name',)
       desc = request.POST.get('desc', )
       char = request.POST.get('char', )
       img = request.FILES['img']
       cartoon=Cartoon(name=name,desc=desc,char=char,img=img)
       cartoon.save()
    return render(request,'add.html')
def edit(request,id):
    cartoon=Cartoon.objects.get(id=id)
    form=CartoonForm(request.POST or None,request.FILES,instance=cartoon)
    if form.is_valid():
        form.save()
        return redirect('/')
    return  render(request,'edit.html',{'form':form,'cartoon':cartoon})

def delete(request,id):
    if request.method =='POST':
        cartoon=Cartoon.objects.get(id=id)
        cartoon.delete()
        return redirect('/')
    return render(request,'delete.html')