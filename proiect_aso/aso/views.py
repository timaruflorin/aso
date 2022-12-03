from django.shortcuts import render, redirect

from .forms import SignUpForm
from django.contrib.auth import login
# Create your views here.


def homepage(request):
    return render(request, 'home/home.html')


def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('homepage')
    else:
        form = SignUpForm()
    return render(request, 'home/register.html', {'form': form})
