from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name ='Fizzle-Home'),
    path('about/', views.about, name ='Fizzle-About'),
    path('login/', views.login, name ='Fizzle-Login'),
    path('register/', views.register, name = 'Fizzle-Register')
]