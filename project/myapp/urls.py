"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('index', views.index, name='index'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('admin_login', views.admin_login, name='admin_login'),
    path('admin_changepassword', views.admin_changepassword, name='admin_changepassword'),
    path('admin_logout', views.admin_logout, name='admin_logout'),
    path('admin_home', views.admin_home, name='admin_home'),

    path('admin_doctor_master_add', views.admin_doctor_master_add, name='admin_doctor_master_add'),
    path('admin_doctor_master_view', views.admin_doctor_master_view, name='admin_doctor_master_view'),
    path('admin_symptom_master_add', views.admin_symptom_master_add, name='admin_symptom_master_add'),
    path('admin_symptom_master_view', views.admin_symptom_master_view, name='admin_symptom_master_view'),
    path('admin_disease_master_add', views.admin_disease_master_add, name='admin_disease_master_add'),
    path('admin_disease_master_view', views.admin_disease_master_view, name='admin_disease_master_view'),
    path('admin_disease_symptom_map_add', views.admin_disease_symptom_map_add, name='admin_disease_symptom_map_add'),
    path('admin_disease_symptom_map_view', views.admin_disease_symptom_map_view, name='admin_disease_symptom_map_view'),
    path('admin_disease_drug_map_add', views.admin_disease_drug_map_add, name='admin_disease_drug_map_add'),
    path('admin_disease_drug_map_view', views.admin_disease_drug_map_view, name='admin_disease_drug_map_view'),
    path('admin_disease_treatment_add', views.admin_disease_treatment_add, name='admin_disease_treatment_add'),
    path('admin_disease_treatment_view', views.admin_disease_master_add, name='admin_disease_treatment_view'),
    path('admin_drug_master_add', views.admin_drug_master_add, name='admin_drug_master_add'),
    path('admin_drug_master_view', views.admin_drug_master_view, name='admin_drug_master_view'),

    path('user_login', views.user_login_check, name='user_login'),
    path('user_logout', views.user_logout, name='user_logout'),
    path('user_home', views.user_home, name='user_home'),
    path('user_details_add', views.user_details_add, name='user_details_add'),
    path('user_changepassword', views.user_changepassword, name='user_changepassword'),

]
