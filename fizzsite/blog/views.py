from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.decorators import login_required
from users.forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib import messages

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

@login_required
def upload_picture(request):
    return render(request, 'blog/upload_picture.html', {'title': 'quiz'})

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('Fizzle-Profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'users/profile.html', context)


class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('Fizzle-Login')
    template_name = 'users/register.html'


