from django.urls import path, include
from Business import views
# Create your urls here
urlpatterns = [
    path('index/', views.index, name='index'),
]