from django.shortcuts import render, HttpResponseRedirect
from django.views.generic import ListView, CreateView
from .models import Expense
from .forms import create_form
from django.urls import reverse
from django.db.models import Sum
from django.contrib import messages
from account.decorators import allowed_users
# Create your views here.


# Inventory
def Home(request):
    total_expense = Expense.objects.all().aggregate(Sum('amount'))
    context = {
        'object_list' : Expense.objects.all(),
        'total' : total_expense['amount__sum']
    }
    # salaryobj = Salary.objects.filter(employee=emp_id,created_at__month=today.month).aggregate(Sum('amount'))
    return render(request, 'expense.html', context)


def Add(request):
    form = create_form(request.POST or None)

    if form.is_valid():
        form.save()
        messages.error(request, 'Your actions have been succesfully saved !')
        return HttpResponseRedirect(reverse('expense:home'))

        
    return render(request, 'expense-add.html', {'form': form})


@allowed_users(allowed_roles=['Administrator'])
def Edit(request, pk):
    object = Expense.objects.get(id=pk)
    form = create_form(request.POST or None, instance=object)

    if form.is_valid():
        form.save()
        request.session['message'] = True
        return HttpResponseRedirect(reverse('expense:home'))
    
    return render(request, 'expense-edit.html', {'form': form})


@allowed_users(allowed_roles=['Administrator'])
def Delete(request):
    pk = request.POST['product']
    object = Expense.objects.get(id=pk)
    object.delete()
    messages.error(request, 'Your actions have been succesfully saved !')
    return HttpResponseRedirect(reverse('expense:home'))

