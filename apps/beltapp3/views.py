from django.shortcuts import render, HttpResponse, redirect, reverse
from .models import Item
from ..loginreg.models import User
from django.contrib import messages

def index(request):
    if 'id' not in request.session:
        return redirect(reverse('loginreg:index'))
    user = User.objects.get(id=request.session["id"])
    context = {
        "items":Item.objects.all(),
        "me": (Item.objects.filter(creator=user) | Item.objects.filter(adders__id=user.id)).distinct(),
        "notme": Item.objects.all().exclude(creator=user).exclude(adders__id=user.id)
    }
    return render(request, 'beltapp3/index.html', context)

def add(request):
    if 'id' not in request.session:
        return redirect(reverse('loginreg:index'))
    return render(request, 'beltapp3/add.html')

def create(request):
    if 'id' not in request.session:
        return redirect(reverse('loginreg:index'))

    if len(request.POST["item_name"]) > 3:
        user = User.objects.get(id=request.session['id'])
        item = request.POST["item_name"]
        Item.objects.create(item_name=item, creator=user)
        return redirect(reverse('beltapp3:index'))
    else:
        messages.add_message(request, messages.SUCCESS, 'Your Item Needs to Be Longer Than 3 Characters')
        return redirect(reverse('beltapp3:add'))

def update(request, item_id):
    if 'id' not in request.session:
        return redirect(reverse('loginreg:index'))

    userid = User.objects.get(id=request.session['id'])
    selected_item = Item.objects.get(id=item_id)
    selected_item.adders.add(userid)
    return redirect(reverse('beltapp3:index'))

def show(request, item_id):
    if 'id' not in request.session:
        return redirect(reverse('loginreg:index'))
    context = {
        "item": Item.objects.get(id=item_id),
        "users": User.objects.all()
    }
    return render(request, 'beltapp3/show.html', context)

def edit(request, item_id):
    if 'id' not in request.session:
        return redirect(reverse('loginreg:index'))
    userid = User.objects.get(id=request.session['id'])
    selected_item = Item.objects.get(id=item_id)
    selected_item.adders.remove(userid)
    return redirect(reverse('beltapp3:index'))

def delete(request, item_id):
    if 'id' not in request.session:
        return redirect(reverse('loginreg:index'))

    context = {
        "item": Item.objects.get(id=item_id),
        "users": User.objects.all()
    }
    return render(request, 'beltapp3/delete.html', context)

def destroy(request, item_id):
    if 'id' not in request.session:
        return redirect(reverse('loginreg:index'))
    item = Item.objects.get(id=item_id)
    item.delete()
    return redirect(reverse('beltapp3:index'))
