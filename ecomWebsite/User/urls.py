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
    # path('', include('Store.urls', namespace='product')),
    path('product/<str:pk>', views.product, name='product'),


    path('user/profile/', views.reguserProfile, name='userProfile'),
    path('business/interface/', views.businessInterface, name='businessInterface'),
    path('store/', include('Store.urls', namespace='Store')),


    path('add_to_cart/<str:pk>/', views.add_to_cart, name='add_to_cart'),
    path('remove_from_cart/<str:pk>/', views.remove_from_cart, name='remove_from_cart'),
    path('cart', views.cart, name='cart'),
    path('cart_product/<str:pk>/', views.cart_product, name='cart_product'),
]