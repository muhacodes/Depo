from django.shortcuts import render, HttpResponseRedirect
from django.views.generic import ListView, CreateView
from .models import inventories
from .forms import create_form
from django.urls import reverse
from django.db.models import Sum
from django.contrib import messages
from account.decorators import allowed_users
# Create your views here.


# Inventory
@allowed_users(allowed_roles=['Administrator'])
def Home(request):
    context = {
        'object_list' : inventories.objects.all()
    }
    return render(request, 'inv.html', context)


def Add(request):
    form = create_form(request.POST or None)

    if form.is_valid():
        form.save()
        messages.error(request, 'Your actions have been succesfully saved !')
        return HttpResponseRedirect(reverse('inventory:home'))

        
    return render(request, 'Inventory-add.html', {'form': form})


def Edit(request, pk):
    object = inventories.objects.get(id=pk)
    form = create_form(request.POST or None, instance=object)

    if form.is_valid():
        form.save()
        request.session['message'] = True
        return HttpResponseRedirect(reverse('inventory:home'))
    
    return render(request, 'Inventory-edit.html', {'form': form})


def Delete(request):
    pk = request.POST['product']
    object = inventories.objects.get(id=pk)
    object.delete()
    messages.error(request, 'Your actions have been succesfully saved !')
    return HttpResponseRedirect(reverse('inventory:home'))

