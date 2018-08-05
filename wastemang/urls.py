# my_project/urls.py
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
from . import views

urlpatterns = [
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    #path('login/','django.contrib.auth.views.login', {'template_name': '/login.html'}),
    #path('signup/', views.signup, name='signup'),
    path('sell/',TemplateView.as_view(template_name = 'sell.html'),name = 'sell'),
    path('details/', views.HomeView.as_view(), name='details'),
    path('thank/', TemplateView.as_view(template_name='thank.html'), name='thank'),
]