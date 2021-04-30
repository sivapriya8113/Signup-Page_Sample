from django.shortcuts import render, redirect
from django.contrib.auth import logout
# Create your views here.
from myapp.models import register


def reg(request):
    if request.method == 'POST':

        member = register(firstName=request.POST['firstname'], lastName=request.POST['lastname'],
                          phoneNo=request.POST['phno'], email=request.POST['mail'],
                          password=request.POST['password'],)
        member.save()
        return redirect('/')
    else:
        return render(request, 'registraction.html')


def login(request):
    return render(request, 'login.html')


def home(request):
    if request.method == 'POST':
        if register.objects.filter(firstName=request.POST['username'], password=request.POST['password']).exists():
            member = register.objects.get(firstName=request.POST['username'], password=request.POST['password'])
            return render(request, 'home.html', {'member': member})
        else:
            context = {'msg': 'Invalid username or password'}
            return render(request, 'login.html', context)

def logout(request):
    logout(request)
    return redirect('registraction.html')