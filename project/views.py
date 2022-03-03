from urllib import request
from django.shortcuts import render, HttpResponse, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.db.models import Sum
from Product.models import products
from Expense.models import Expense
from Sales.models import Sale
from django.db.models import Sum, F
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from account.forms import ChangePasswordForm
from account.forms import CreateUser 


def home(request):

    total_products = products.objects.all().count()
    total_expense = Expense.objects.all().aggregate(Sum('amount'))
    total_sales = Expense.objects.all().aggregate(Sum('amount'))
    total_number_of_sales =  Sale.objects.all().count()

    context = {
        'products' : total_products,
        'expense' : total_expense['amount__sum'],
        'total_sales' : Sale.objects.filter().aggregate(sum=Sum(F('quantity')*F('selling_price')))["sum"],
        'sales_total' : total_number_of_sales,
    }

    return render(request, 'home.html', context)


def index(request):
    return HttpResponseRedirect(reverse('home'))



def settings(request):
    if request.method == 'POST':
        form = ChangePasswordForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('home')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = ChangePasswordForm(request.user)
    return render(request, 'changepassword.html', {
        'form': form
    })



def UserCreation(request):
    form = CreateUser(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect(to='home')

    return render(request, 'registerUser.html', {'form' : form, 'errors' : form.errors})