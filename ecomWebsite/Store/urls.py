from django.urls import path
from Store import views
from Store.forms import *

# Create your urls here
app_name = 'Store'
urlpatterns = [
    path('', views.store, name='mainStore'),
    path('product/', views.product, name='product'),
]