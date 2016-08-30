from django.shortcuts import render, HttpResponse, redirect
# from .models import People

def index(request):
    context = { "somekey":"somevalue" }
    return render(request, 'beltapp3/index.html', context)

# def show(request):
#     print(request.method)
#     return render(request, 'beltapp3/show_users.html')
