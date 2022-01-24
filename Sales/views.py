from django.shortcuts import render, HttpResponseRedirect
from django.views.generic import ListView, CreateView
from .models import Sale
from .forms import create_form
from django.urls import reverse
from django.db.models import Sum
from django.contrib import messages
from django.db.models import F
from django.db.models import Sum, F
from account.decorators import allowed_users
# Create your views here.


# sales
@allowed_users(allowed_roles=['Administrator', 'employee'])
def Home(request):
    # total_sales = Sale.objects.all().aggregate(Sum('amount'))
    # total_sales = Sale.objects.extra(select={'total': "quantity * selling_price "}).aggregate(Sum('total'))
    # total_sales = Sale.objects.filter(type="normal").values('quantity').annotate(amount=Sum('id', field="width * height")
    # total_sales = Sale.objects.all().extra(select={'total': "quantity * selling_price"}).values
    total_sales = Sale.objects.filter().aggregate(sum=Sum(F('quantity')*F('selling_price')))["sum"]
    
    context = {
        'object_list' : Sale.objects.all(),
        'total' : total_sales
    }
    return render(request, 'sales.html', context)


def Add(request):
    form = create_form(request.POST or None)

    if form.is_valid():
        obj  = form.save(commit=False)
        selling_price =    obj.product.selling_price

        if selling_price == None:
            messages.error(request, 'Selling Price is missing !')
            return HttpResponseRedirect(reverse('product:home'))
        
        obj.selling_price =  selling_price
        obj.save()
        messages.error(request, 'Your actions have been succesfully saved !')
        return HttpResponseRedirect(reverse('sales:home'))

        
    return render(request, 'sales-add.html', {'form': form})


@allowed_users(allowed_roles=['Administrator'])
def Edit(request, pk):
    object = Sale.objects.get(id=pk)
    form = create_form(request.POST or None, instance=object)

    if form.is_valid():
        form.save()
        request.session['message'] = True
        messages.error(request, 'Your actions have been succesfully saved !')
        return HttpResponseRedirect(reverse('sales:home'))
    
    return render(request, 'sales-edit.html', {'form': form})


@allowed_users(allowed_roles=['Administrator'])
def Delete(request):
    pk = request.POST['product']
    object = Sale.objects.get(id=pk)
    object.delete()
    messages.error(request, 'Your actions have been succesfully saved !')
    return HttpResponseRedirect(reverse('sales:home'))

