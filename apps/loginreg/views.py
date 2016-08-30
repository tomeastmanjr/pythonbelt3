from django.shortcuts import render, HttpResponse, redirect
from .models import User
from django.contrib import messages


def index(request):
    return render(request, 'loginreg/index.html')

def login(request):
    user = User.objects.login(request.POST)
    if user[0]:
        request.session['username']= user[1].username
        request.session['id']= user[1].id
        return redirect('beltapp3:index')
    messages.add_message(request, messages.ERROR, user[1])
    return redirect('loginreg:index')

def register(request):
    user = User.objects.register(request.POST)
    print user[0], user[1]
    if user[0]:
        request.session['username']= user[1].username
        request.session['id']= user[1].id
        return redirect('beltapp3:index')
    else:
        errors = user[1]
        for error in errors:
            messages.add_message(request, messages.ERROR, error)
    return redirect('loginreg:index')

def logout(request):
    request.session.clear()
    return redirect('loginreg:index')
