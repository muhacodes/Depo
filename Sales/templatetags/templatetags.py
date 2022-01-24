from django import template
from Product.models import products
from django.contrib.humanize.templatetags.humanize import intcomma

register = template.Library()

@register.filter(name='subtract')
def subtract(value, arg):
    return value - arg


#  subtract two arguments and multiply the price 
@register.simple_tag
def price(opens, close, price):
    amount = int(close) - int(opens)
    return intcomma(int(amount * price))


#  multiply  two argumanets eg 10*2
@register.filter(name='multiply')
def x(x,y):
    return x*y

@register.filter(name='add')
def add(x,y):
    return x + y
