from django.shortcuts import render, HttpResponse, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.db.models import Sum
from Product.models import products
from Expense.models import Expense
from Sales.models import Sale
from django.db.models import Sum, F

def home(request):

    total_products = products.objects.all().aggregate(Sum('cost_price'))
    total_expense = Expense.objects.all().aggregate(Sum('amount'))
    total_sales = Expense.objects.all().aggregate(Sum('amount'))
    
    context = {
        'products' : total_products['cost_price__sum'],
        'expense' : total_expense['amount__sum'],
        'total_sales' : Sale.objects.filter().aggregate(sum=Sum(F('quantity')*F('selling_price')))["sum"]
    }

    return render(request, 'home.html', context)


def index(request):
    return HttpResponseRedirect(reverse('home'))