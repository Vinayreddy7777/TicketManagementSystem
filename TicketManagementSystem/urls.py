"""TicketManagementSystem URL Configuration

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
from django.urls import path
from mainapp import views as main_views
from adminapp import views as admin_views
from userapp import views as user_views


urlpatterns = [
    #main
    path('admin/', admin.site.urls),
    path('', main_views.main_home, name='main_home'),
    
    
    
    
    #admin
    path('admin', admin_views.admin_login, name='admin_login'),
    path('admin-home',admin_views.admin_home, name='admin_home'),
    path('accept_ticket/<int:id>/',admin_views.accept_ticket, name='accept_ticket'),
    path('reject_ticket/<int:id>/',admin_views.reject_ticket, name='reject_ticket'),
    path('',main_views.main_home, name='admin_logout'),
    
    
    
    #user
    path('user-login', user_views.user_login, name='user_login'),
    path('user-registration',user_views.user_register,name='user_register'),
    path('user-home',user_views.user_home, name='user_home'),
    path('user-view',user_views.user_view, name='user_view'),
    path('user-edit/<int:id>/',user_views.user_edit, name='user_edit'),
    path('user-status',user_views.user_status, name='user_status'),
    path('',main_views.main_home, name='user_logout'),

]
