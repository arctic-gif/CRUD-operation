from core.views import *
from django.conf.urls.static import static
from django.conf import settings
"""
URL configuration for website project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
urlpatterns = [
    path('admin/', admin.site.urls, name='super'),
    path('',home,name='home'),
    path('register/',register,name='register'),
    path('regorlog/',regorlog,name='regorlog'),
    path('view/',viewcustomer,name='view'),
    path('edit/<int:id>',editcustomer,name='edit'),
    path('delete/<int:id>',deletecustomer,name='delete'),
    path('productreg/',registerproduct,name='proreg'),
    path('viewproducts/',viewproduct,name='viewproduct'),
    path('editproduct/<int:id>',editproduct,name='editproduct'),
    path('deleteproduct/<int:id>',deleteproduct,name='deleteproduct'),
    path('contactus/',contactus,name='contactus')
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)