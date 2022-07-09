from django.urls import path, include
from User import views
# Create your urls here
urlpatterns = [
    path('index/', views.index, name='index'),
    path('user/register/', views.userRegister, name='userregister'),
    path('business/register/', views.businessRegister, name='businessregister'),
    path('user/login/', views.userLogin, name='userlogin'),
    path('business/login/', views.businessLogin, name='businesslogin'),
    path('user/logout/', views.userLogout, name='userlogout'),
    path('', include('Store.urls', namespace='product')),


    path('user/profile/', views.reguserProfile, name='userProfile'),
]