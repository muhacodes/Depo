from django.shortcuts import render, HttpResponseRedirect
from django.views.generic import ListView, CreateView
from .models import clear
from .forms import create_form
from django.urls import reverse
from django.db.models import Sum
from django.contrib import messages
from account.decorators import allowed_users
# Create your views here.


# clearance
def Home(request):
    total = clear.objects.all().aggregate(Sum('amount'))
    context = {
        'object_list' : clear.objects.all(),
        'total' : total['amount__sum']
    }
    return render(request, 'clearance.html', context)


def Add(request):
    form = create_form(request.POST or None)

    if form.is_valid():
        form.save()
        messages.error(request, 'Your actions have been succesfully saved !')
        return HttpResponseRedirect(reverse('clearance:home'))

        
    return render(request, 'clearance-add.html', {'form': form})



@allowed_users(allowed_roles=['Administrator'])
def Edit(request, pk):
    object = clear.objects.get(id=pk)
    form = create_form(request.POST or None, instance=object)

    if form.is_valid():
        form.save()
        request.session['message'] = True
        return HttpResponseRedirect(reverse('clearance:home'))
    
    return render(request, 'clearance-edit.html', {'form': form})


@allowed_users(allowed_roles=['Administrator'])
def Delete(request):
    pk = request.POST['product']
    object = clear.objects.get(id=pk)
    object.delete()
    messages.error(request, 'Your actions have been succesfully saved !')
    return HttpResponseRedirect(reverse('clearance:home'))

