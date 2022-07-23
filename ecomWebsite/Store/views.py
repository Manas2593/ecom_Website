from django.shortcuts import redirect, render
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.urls import reverse
from Store.forms import ProductCreationForm
from Store.models import Product

# Create your views here.

def store(request):
    reguser = request.user
    context = {'reguser':reguser}
    return render(request, 'Store/index.html', context)

# def listProduct(request):
#     reguser = request.user
#     form = ProductCreationForm(instance=reguser)
#     if request.method == 'POST':
#         form = ProductCreationForm(request.POST, request.FILES, instance=reguser)
#         if form.is_valid():
#             form.owner.set(reguser)
#             return redirect('Store:mainStore')
#         else :
#             return messages.error(reguserquest, 'Errors')
#     context = {'form':form}
#     return render(request, 'Store/product_registration.html', context)
def listProduct(request):
    reguser = request.user
    form = ProductCreationForm()
    if request.method == 'POST':
        form = ProductCreationForm(request.POST, request.FILES)
        if form.is_valid():
            regproduct = form.save(commit=False)
            regproduct.owner = reguser
            regproduct.save()
            form.save_m2m()
            return redirect(reverse('Store:mainStore'))
        else:
            return messages.error(request, 'Errors')
    context = {'form':form}
    return render(request, 'Store/product_registration.html', context)