from django.shortcuts import render

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
    return render(request, 'blog/login.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})

def register(request):
    return render(request, 'users/register.html', {'title': 'Register'})

