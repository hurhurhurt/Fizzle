from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name ='Fizzle-Home'),
    path('about/', views.about, name ='Fizzle-About'),
    path('', include('django.contrib.auth.urls')),
    path('login/', views.login, name ='Fizzle-Login'),
    path('logout/', views.login, name ='Fizzle-Logout'),
    path('register/', views.register, name = 'Fizzle-Register')
]