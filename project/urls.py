"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [

    path('', views.index, name='index' ),

    path('administrator/', admin.site.urls),

    path('admin/user/', include('account.urls')),

    path('admin/dashboard', login_required(views.home), name='home'),

    # # path('admin/inventory/', include('Inventory.urls', 'inventory')),

    # # path('admin/product/', include('Product.urls', 'product')),

    # # path('admin/employee/', include('Employee.urls', 'employee')),

    # # path('admin/sales/', include('Sales.urls', 'sales')),

    path('admin/', include('Clearance.urls')),

    path('admin/', include('Employee.urls')),
    
    path('admin/', include('Expense.urls')),

    path('admin/', include('Inventory.urls')),

    path('admin/', include('Inventory.Truckexp')),

    path('admin/', include('Product.urls')),

    path('admin/', include('Salary.urls')),

    path('admin/', include('Sales.urls')),

    path('admin/', include('Rate.urls')),

    path('admin/settings-change-password', views.settings, name='settings-change-password'),

    path('admin/settings-create-user', views.UserCreation, name='settings-create-user'),


    
]

if settings.DEBUG:
     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)