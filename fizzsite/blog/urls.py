from django.http import request
from django.urls import path, include
from django.conf import settings
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from . import views
from users import views as user_views

urlpatterns = [
    path('', views.home, name='Fizzle-Home'),
    path('about/', views.about, name='Fizzle-About'),
    path('', include('django.contrib.auth.urls')),
    path('profile/', views.profile, name='Fizzle-Profile'),
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='Fizzle-Login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='blog/logout.html'), name='Fizzle-Logout'),
    path('register/', views.SignUp.as_view(), name='Fizzle-Register'),
    path('upload_picture/', views.upload_picture, name='Fizzle-Upload_Picture'),
    path('questions/', views.questions, name='Fizzle-Questions'),
    path('match/', views.match, name='Fizzle-Match'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
