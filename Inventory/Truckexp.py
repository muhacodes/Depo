"""Depo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import TruckExpViews
from django.contrib.auth.decorators import login_required


app_name = 'truck-exp'

urlpatterns = [
    path('TruckExpense', login_required(TruckExpViews.Home), name='home'),

    path('truck-expense/add/', login_required(TruckExpViews.Add), name='add'),

    path('truck-expense/edit/<int:pk>', login_required(TruckExpViews.Edit), name='edit'),

    path('truck-expense/delete', login_required(TruckExpViews.Delete), name='delete'),

]
