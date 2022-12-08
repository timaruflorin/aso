from django.shortcuts import render, redirect

from .forms import SignUpForm, RoomForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.utils.text import slugify
from .models import Room, Message

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


@login_required
def rooms(request):
    rooms = Room.objects.all()
    return render(request, 'room/rooms.html', {'rooms': rooms})


@login_required
def room(request, slug):
    room = Room.objects.get(slug=slug)
    messages = Message.objects.filter(room=room)[0:25]

    return render(request, 'room/room.html', {'room': room, 'messages': messages})


@login_required
def createroom(request):
    if request.POST:
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('rooms')
            
    return render(request, 'room/createroom.html', {'form': RoomForm})
