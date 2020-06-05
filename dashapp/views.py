from django.shortcuts import render
from .models import country

def index(request):
    qs = country.objects.all()
    context = {
        "qs":qs
    }
    return render(request, 'dashapp/index.html', context)


def DashView(request):
    return render(request, 'dashapp/dash.html')



def AddView(request):
    return render(request, 'dashapp/add.html')
