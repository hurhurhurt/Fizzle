from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.home, name ='Fizzle-Home'),
    path('about/', views.about, name ='Fizzle-About'),
    path('', include('django.contrib.auth.urls')),
    path('profile/', views.profile, name = 'Fizzle-Profile'),
    path('login/', views.login, name ='Fizzle-Login'),
    path('logout/', views.login, name ='Fizzle-Logout'),
    path('register/', views.SignUp.as_view(), name = 'Fizzle-Register'),
    path('upload_picture/', views.upload_picture, name = 'Fizzle-Upload_Picture')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

