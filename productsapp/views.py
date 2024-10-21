from django.shortcuts import render,redirect
from .forms import createForm
from .models import Product
from django.core.paginator import Paginator

# Create your views here.
def product_create(request):
    if request.method == 'POST':
        form = createForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('read')
    else:
        form = createForm()
    return render(request,'create.html', {'form':form} )  

def product_read(request):
    product_list = Product.objects.all()
    return render(request,'read.html',{'product_list': product_list })

# def product_update(request,pk):
#     product = Product.objects.get(pk=pk) 
#     if request.method == 'POST':
#         form = Product(request.POST,instance=product)
#         if form.is_valid():
#             form.save()
#             return redirect('read')
#     else:
#         form = Product(instance=product)
#     return render(request,'update.html',{'form':form})             
def product_update(request, pk):
    product = Product.objects.get(pk=pk)  # Get the product instance
    if request.method == 'POST':
        form = createForm(request.POST, instance=product)  # Use the form class
        if form.is_valid():
            form.save()
            return redirect('read')
    else:
        form = createForm(instance=product)  # Use the form class here as well
    return render(request, 'update.html', {'form': form})
def product_delete(request,pk):
    product = Product.objects.get(pk=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('read')
    return render(request,'delete.html',{'product':product})

def listing(request):
    product_list = Product.objects.all()
    paginator = Paginator(product_list,2)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render (request,'list.html',{'page_obj':page_obj})