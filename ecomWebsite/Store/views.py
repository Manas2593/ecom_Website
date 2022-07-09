from django.shortcuts import render

# Create your views here.

def store(request):
    context = {}
    return render(request, 'Store/index.html', context)

def product(request):
    context = {}
    return render(request, 'Store/product.html', context)