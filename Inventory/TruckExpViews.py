from django.shortcuts import render, HttpResponseRedirect
from django.views.generic import ListView, CreateView
from .models import TruckExpense
from .forms import TruckExpForm
from django.urls import reverse
from django.db.models import Sum
from django.contrib import messages
from account.decorators import allowed_users
# Create your views here.


# Inventory
@allowed_users(allowed_roles=['Administrator'])
def Home(request):
    context = {
        'object_list' : TruckExpense.objects.all()
    }
    return render(request, 'Truck-expense.html', context)


def Add(request):
    form = TruckExpForm(request.POST or None)

    if form.is_valid():
        form.save()
        messages.error(request, 'Your actions have been succesfully saved !')
        return HttpResponseRedirect(reverse('truck-exp:home'))

        
    return render(request, 'Truck-expense-add.html', {'form': form})


def Edit(request, pk):
    object = TruckExpense.objects.get(id=pk)
    form = TruckExpForm(request.POST or None, instance=object)

    if form.is_valid():
        form.save()
        request.session['message'] = True
        return HttpResponseRedirect(reverse('truck-exp:home'))
    
    return render(request, 'Truck-expense-add.html', {'form': form})


def Delete(request):
    pk = request.POST['product']
    object = TruckExpense.objects.get(id=pk)
    object.delete()
    messages.error(request, 'Your actions have been succesfully saved !')
    return HttpResponseRedirect(reverse('truck-exp:home'))

