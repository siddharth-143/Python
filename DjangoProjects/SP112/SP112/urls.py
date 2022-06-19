"""SP112 URL Configuration

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
from typing import Pattern
from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from school import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.TemplateView.as_view(template_name='school/home.html'), name='blankhome'),
    path('home/', views.RedirectView.as_view(url='/'), name='home'),

    # path('index/', views.RedirectView.as_view(url='/'), name='index'),
    path('index/', views.RedirectView.as_view(pattern_name='home'), name='index'),

    path('siddhya/', views.RedirectView.as_view(url='https://www.google.com'), name='siddhya'),
    path('siddhya/', views.SiddhyaRedirectView.as_view(), name='siddhya'),

    path('home/<int:pk>/', views.VentyaRedirectView.as_view(), name='ventya'),
    path('<int:pk>/', views.TemplateView.as_view(template_name='school/home.html'), name='mindex'),

    # path('home/<slug:post>/', views.VentyaRedirectView.as_view(), name='ventya'),
    # path('/<slug:post>/', views.TemplateView.as_view(template_name='school/home.html'), name='mindex'),
]
