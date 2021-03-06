from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from User.forms import createregUser, userProfileForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from User.models import userProfile
from Store.models import Product

# Create your views here.
@login_required(login_url='userlogin')
def index(request):
    products = Product.objects.all()
    reguser = request.user
    regusername = str(reguser.userprofile.first_name) + ' ' + str(reguser.userprofile.last_name)
    context = {'reguser':reguser, 'regusername':regusername, 'products':products}
    return render(request, 'User/index.html', context)


def userRegister(request):
    form = createregUser()
    if request.method == 'POST':
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        if password1 != password2:
            return redirect('userregister')
            #  messages.error(request, "Password doesn't match. Try again!")
        else:
            form = createregUser(request.POST)
            if form.is_valid():
                regUser = form.save()
                userProfile.objects.create(
                    user = regUser
                )
                return redirect('userlogin')
            else:
                return messages.error(request, 'User already registered. Sign in!')

    context = {'form':form}
    return render(request, 'User/userregister.html', context)




def businessRegister(request):
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
                return messages.error(request, 'Business already listed. Sign in!')

    context = {'form':form}
    return render(request, 'User/businessregister.html', context)





def userLogin(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('userProfile')
        else:
            messages.error(request, 'User not registered.')
    context = {}
    return render(request, 'User/userlogin.html', context)



def businessLogin(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('businessInterface')
        else:
            messages.error(request, 'Business not registered.')
    context = {}
    return render(request, 'User/businesslogin.html', context)


@login_required(login_url='businesslogin')
def businessInterface(request):
    context = {}
    return render(request, 'User/business_interface.html', context)







def userLogout(request):
    logout(request)
    return redirect('userlogin')






# Profiles
@login_required(login_url='userlogin')
def reguserProfile(request):
    reguser = request.user
    reguserprofile = reguser.userprofile
    form = userProfileForm(instance=reguserprofile)
    if request.method == 'POST':
        form = userProfileForm(request.POST, instance=reguserprofile)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            return ValueError('Problem submitting form currently. Try again after some time.')
    context = {'form':form, 'reguser':reguser}
    return render(request, 'User/userProfile.html', context)




def product(request, pk):
    reguser = request.user.userprofile
    regusername = str(reguser.first_name) + ' ' + str(reguser.last_name)
    singleproduct = get_object_or_404(Product, id=pk)
    context = {'singleproduct':singleproduct, 'regusername':regusername}
    return render(request, 'User/product.html', context)


def add_to_cart(request, pk):
    user = request.user.userprofile
    singleproduct = get_object_or_404(Product, id=pk)
    singleproduct.procuring_user = user
    singleproduct.save()
    return redirect('index')


def remove_from_cart(request, pk):
    user = request.user.userprofile
    singleproduct = get_object_or_404(Product, id=pk)
    singleproduct.procuring_user = None
    singleproduct.save()
    return redirect('cart')

def cart(request):
    reguser = request.user
    user = reguser.userprofile
    allproducts = Product.objects.filter(procuring_user=user)
    context = {'allproducts':allproducts, 'user':user}
    return render(request, 'User/cart.html', context)


def cart_product(request, pk):
    reguser = request.user.userprofile
    regusername = str(reguser.first_name) + ' ' + str(reguser.last_name)
    singleproduct = get_object_or_404(Product, id=pk)
    context = {'singleproduct':singleproduct, 'regusername':regusername}
    return render(request, 'User/cart_product.html', context)