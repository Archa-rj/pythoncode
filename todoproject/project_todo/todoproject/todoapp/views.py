from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .models import Task
from .forms import TodoForm
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import UpdateView
from django.views.generic import DeleteView
class TaskListview(ListView):
    model=Task
    template_name = 'home.html'
    context_object_name ='detail'

class TaskDetailview(DetailView):
    model = Task
    template_name = 'details.html'
    context_object_name ='detail'

class TaskUpdateview(UpdateView):
    model = Task
    template_name = 'update.html'
    context_object_name = 'detail'
    fields = ('name','priority','date')

    def get_success_url(self):
        return reverse_lazy('cbvdetail',kwargs={'pk':self.object.id})

class TaskDeleteview(DeleteView):
    model = Task
    template_name = 'delete.html'
    success_url = reverse_lazy('cbvhome')

# Create your views here.
def add(request):
    det=Task.objects.all()
    if request.method=='POST':
        name=request.POST.get('task','')
        priority=request.POST.get('priority','')
        date=request.POST.get('date','')
        task=Task(name=name,priority=priority,date=date)
        task.save()
    return render(request,'home.html',{'detail':det})

# def details(request):
#     task=Task.objects.all()
#     return render(request,'details.html',{'task':task})

def delete(request,taskid):
    task = Task.objects.get(id=taskid)
    if request.method=='POST':

        task.delete()
        return redirect('/')
    return render(request,'delete.html')

def edit(request,id):
    task=Task.objects.get(id=id)
    forms=TodoForm(request.POST or None,instance=task)
    if forms.is_valid():
        forms.save()
        return redirect('/')
    return render(request,'edit.html',{'form':forms,'task1':task})