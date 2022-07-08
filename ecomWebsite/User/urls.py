from django.urls import path, include
from User import views
# Create your urls here
urlpatterns = [
    path('index/', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutPage, name='logout'),
]