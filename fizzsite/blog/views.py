from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

posts = [
    {
        'author': 'Fizzle',
        'title': 'Post 1',
        'content': 'First Post',
        'Date_Posted': 'Feb 8th'
    },
    {
        'author': 'Fizzle',
        'title': 'Post 2',
        'content': 'Second Post',
        'Date_Posted': 'Feb 9th'
    }
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/base.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})

def login(request):
    return render(request, 'blog/login.html', {'title': 'Login'})

def register(request):
    return render(request, 'users/register.html', {'title': 'Register'})

def upload_picture(request):
    return render(request, 'blog/upload_picture.html', {'title': 'quiz'})

def profile(request):
    return render(request, 'users/profile.html', {'title': 'Profile'})

class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('Fizzle-Login')
    template_name = 'users/register.html'


