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
from . import views
from django.contrib.auth.decorators import login_required


app_name = 'employee'

urlpatterns = [
    path('employee', login_required(views.Home), name='home'),

    path('employee/add/', login_required(views.Add), name='add'),

    path('employee/edit/<int:pk>', login_required(views.Edit), name='edit'),

    path('employee/delete', login_required(views.Delete), name='delete'),


]
