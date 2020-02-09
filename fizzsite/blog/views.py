from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.decorators import login_required
from users.forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm, QuestionsForm
from django.contrib import messages
from blog.models import Quiz

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})

def login(request):
    return render(request, 'blog/login.html', {'title': 'Login'})

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('Fizzle-Register')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

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

@login_required
def questions(request):
    if request.method == 'POST':
        q_form = UserUpdateForm(request.POST, instance=request.user)

        if q_form.is_valid():
            q_form.save()
            messages.success(request, f'Questions answered')
            return redirect('Fizzle-Profile')

    else:
        q_form = QuestionsForm(instance=request.user.questions)

    context = {
        'q_form': q_form
    }

    return render(request, 'users/quiz.html', context)

@login_required
def quiz(request):
    if request.method == 'POST':
        form = Quiz(request.POST)
        if form.is_valid():
            form.save()
            form.questions = request.user
            return redirect('Fizzle-Quiz')
    else:
        form = Quiz()
    return render(request, 'blog/quiz.html', {'form': form})

class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('Fizzle-Login')
    template_name = 'users/register.html'




