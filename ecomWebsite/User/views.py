from django.shortcuts import redirect, render
from django.contrib import messages
from User.forms import createregUser
from django.contrib.auth import login, logout, authenticate

# Create your views here.
def index(request):
    context = {}
    return render(request, 'User/index.html', context)


def register(request):
    form = createregUser()
    if request.method == 'POST':
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        if password1 != password2:
            return messages.error(request, "Password doesn't match. Try again!")
        else:
            form = createregUser(request.POST)
            if form.is_valid():
                form.save()
            else:
                return messages.error(request, 'User already registered. Sign in!')

    context = {'form':form}
    return render(request, 'User/register.html', context)





def loginPage(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'User not registered.')
    context = {}
    return render(request, 'User/login.html', context)


def logoutPage(request):
    logout(request)
    return redirect('login')