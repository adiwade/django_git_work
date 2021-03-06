"""test_git URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from app import views
from email_git import views as eg
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.show_message, name = 'simple view'),

    path('add/', views.show_add, name = 'simple view'),

    path('sub/', views.show_sub, name = 'sub view'),
    path('div/', views.show_div, name = 'div view'),
    path('email/', eg.email_git, name = 'emailgit'),

]
