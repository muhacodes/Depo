from django.shortcuts import render, HttpResponseRedirect
from django.views.generic import ListView, CreateView
from .models import Employee
from .forms import create_form
from django.urls import reverse
from django.db.models import Sum
from django.contrib import messages
from account.decorators import allowed_users
# Create your views here.


# employee
def Home(request):
    context = {
        'object_list' : Employee.objects.all()
    }
    return render(request, 'employee.html', context)


def Add(request):
    form = create_form(request.POST or None)

    if form.is_valid():
        form.save()
        messages.error(request, 'Your actions have been succesfully saved !')
        return HttpResponseRedirect(reverse('employee:home'))

        
    return render(request, 'employee-add.html', {'form': form})



@allowed_users(allowed_roles=['Administrator', 'employee'])
def Edit(request, pk):
    object = Employee.objects.get(id=pk)
    form = create_form(request.POST or None, instance=object)

    if form.is_valid():
        form.save()
        request.session['message'] = True
        return HttpResponseRedirect(reverse('employee:home'))
    
    return render(request, 'employee-edit.html', {'form': form})


@allowed_users(allowed_roles=['Administrator'])
def Delete(request):
    pk = request.POST['product']
    object = Employee.objects.get(id=pk)
    object.delete()
    messages.error(request, 'Your actions have been succesfully saved !')
    return HttpResponseRedirect(reverse('employee:home'))

