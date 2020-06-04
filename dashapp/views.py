from django.shortcuts import render
from .models import country

def index(request):
    qs = country.objects.all()
    context = {
        "qs":qs
    }
    return render(request, 'dashapp/index.html', context)


def room(request, room_name):
    return render(request, 'dashapp/room.html', {
        'room_name': room_name
    })



def AddView(request, room_name):
    return render(request, 'dashapp/add.html', {
        'room_name': room_name
    })
