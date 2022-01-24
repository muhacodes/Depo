from django import forms
from django.shortcuts import render, HttpResponseRedirect
from django.views.generic import ListView, CreateView

from Employee.models import Employee
from .models import Salary
from .forms import create_form
from django.urls import reverse
from django.db.models import Sum
from django.contrib import messages
from datetime import datetime
from django.forms import forms
from account.decorators import allowed_users
# Create your views here.



# Inventory
@allowed_users(allowed_roles=['Administrator'])
def Home(request):
    context = {
        'object_list' : Salary.objects.all()
    }
    return render(request, 'salary.html', context)


def Add(request):
    form = create_form(request.POST or None)

    if form.is_valid():
        form.save(commit=False)
        emp_id = form.instance.employee
        today = datetime.now()

        salaryobj = Salary.objects.filter(employee=emp_id,created_at__month=today.month).aggregate(Sum('amount'))
        employeeSalary = Employee.objects.get(id=emp_id.id)
        employeeSalaryTaken = salaryobj['amount__sum']
        if employeeSalaryTaken != None:
            employeeSalaryBalance = employeeSalary.amount - employeeSalaryTaken
        else:
            employeeSalaryBalance = employeeSalary.amount
        
        if form.instance.amount <= employeeSalaryBalance:
            form.save()
            messages.error(request, 'Your actions have been succesfully saved !')
            return HttpResponseRedirect(reverse('salary:home'))

        return render(request, 'salary-add.html', {'form': form, 'credit': 0})
        
        
    return render(request, 'salary-add.html', {'form': form})


def Edit(request, pk):
    object = Salary.objects.get(id=pk)
    form = create_form(request.POST or None, instance=object)

    if form.is_valid():
        form.save(commit=False)
        emp_id = form.instance.employee
        today = datetime.now()

        salaryobj = Salary.objects.filter(employee=emp_id,created_at__month=today.month).aggregate(Sum('amount'))
        employeeSalary = Employee.objects.get(id=emp_id.id)
        employeeSalaryTaken = salaryobj['amount__sum']
        employeeSalaryBalance = employeeSalary.amount - employeeSalaryTaken
        
        if form.instance.amount < employeeSalaryBalance:
            form.save()
            messages.error(request, 'Your actions have been succesfully saved !')
            return HttpResponseRedirect(reverse('salary:home'))

        return render(request, 'salary-add.html', {'form': form, 'credit': 0})
    
    return render(request, 'salary-edit.html', {'form': form})


def Delete(request):
    pk = request.POST['product']
    object = Salary.objects.get(id=pk)
    object.delete()
    messages.error(request, 'Your actions have been succesfully saved !')
    return HttpResponseRedirect(reverse('salary:home'))

