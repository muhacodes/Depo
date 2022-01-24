from django.shortcuts import render, HttpResponseRedirect
from django.views.generic import ListView, CreateView
from .models import products
from .forms import create_form
from django.urls import reverse
from django.db.models import Sum
from django.contrib import messages
from account.decorators import allowed_users
# Create your views here.


# Inventory



def Home(request):
    total = products.objects.all().aggregate(Sum('cost_price'))
    context = {
        'object_list' : products.objects.all(),
        'total' : total['cost_price__sum']
    }
    return render(request, 'product.html', context)


def Add(request):
    form = create_form(request.POST or None)

    if form.is_valid():
        form.save()
        messages.error(request, 'Your actions have been succesfully saved !')
        return HttpResponseRedirect(reverse('inventory:home'))

        
    return render(request, 'product-add.html', {'form': form})


@allowed_users(allowed_roles=['Administrator'])
def Edit(request, pk):
    object = products.objects.get(id=pk)
    form = create_form(request.POST or None, instance=object)

    if form.is_valid():
        form.save()
        request.session['message'] = True
        return HttpResponseRedirect(reverse('product:home'))
    
    return render(request, 'product-edit.html', {'form': form})


@allowed_users(allowed_roles=['Administrator'])
def Delete(request):
    pk = request.POST['product']
    object = products.objects.get(id=pk)
    object.delete()
    messages.error(request, 'Your actions have been succesfully saved !')
    return HttpResponseRedirect(reverse('inventory:home'))

