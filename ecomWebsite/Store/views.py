from django.shortcuts import redirect, render
from django.contrib import messages
from django.urls import reverse
from Store.forms import ProductCreationForm

# Create your views here.

def store(request):
    context = {}
    return render(request, 'Store/index.html', context)

def listProduct(request):
    form = ProductCreationForm()
    if request.method == 'POST':
        form = ProductCreationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('Store:mainStore')
        else :
            return messages.error(request, 'Errors')
    context = {'form':form}
    return render(request, 'Store/product_registration.html', context)