from django.shortcuts import render, HttpResponse, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.db.models import Sum
from Product.models import products
from Expense.models import Expense
from Sales.models import Sale
from django.db.models import Sum, F

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