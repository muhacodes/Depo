from django.shortcuts import render, HttpResponseRedirect
from django.views.generic import ListView, CreateView
from .models import Rate
from .forms import create_form
from django.urls import reverse
from django.db.models import Sum
from django.contrib import messages
from account.decorators import allowed_users
# Create your views here.


# rate
def Home(request):
    local = Rate.objects.all().aggregate(Sum('local_currency'))
    dollars = Rate.objects.all().aggregate(Sum('dollars'))
    
    context = {
        'object_list' : Rate.objects.all(),
        'local' : local['local_currency__sum'],
        'dollars' : dollars['dollars__sum'],
    }
    return render(request, 'rate.html', context)


def Add(request):
    form = create_form(request.POST or None)

    if form.is_valid():
        form = form.save(commit=True)
        dollars = form.local_currency / form.rate
        form.dollars = dollars
        form.save()
        messages.error(request, 'Your actions have been succesfully saved !')
        return HttpResponseRedirect(reverse('rate:home'))

        
    return render(request, 'rate-add.html', {'form': form})


@allowed_users(allowed_roles=['Administrator'])
def Edit(request, pk):
    object = Rate.objects.get(id=pk)
    form = create_form(request.POST or None, instance=object)

    if form.is_valid():
        form = form.save(commit=True)
        dollars = form.local_currency / form.rate
        form.dollars = dollars
        form.save()
        messages.error(request, 'Your actions have been succesfully saved !')
        return HttpResponseRedirect(reverse('rate:home'))
    
    return render(request, 'rate-edit.html', {'form': form})


@allowed_users(allowed_roles=['Administrator'])
def Delete(request):
    pk = request.POST['product']
    object = Rate.objects.get(id=pk)
    object.delete()
    messages.error(request, 'Your actions have been succesfully saved !')
    return HttpResponseRedirect(reverse('rate:home'))

