from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm, QuestionsForm


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
        q_form =QuestionsForm(request.POST, instance=request.user)

        if q_form.is_valid():
            q_form.save()
            messages.success(request, f'Questions answered')
            return redirect('Fizzle-Home')

    else:
        q_form = QuestionsForm(instance=request.user.questions)

    context = {
        'q_form': q_form
    }

    return render(request, 'users/quiz.html', context)

def match(request, username):
    user = User.objects.get(username=username)
    return render(request, 'users/match.html', {'username':username, 'user':user})