from . import views
from django.urls import path

urlpatterns = [
    path('base', views.base, name='base'),
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('members', views.members, name='members'),
    path('join', views.join, name='join'),
]
