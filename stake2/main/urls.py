from django.urls import path

from . import views

urlpatterns = [
    path('register/', views.reg, name='reg'),
    path('deposit/', views.money, name='money')
]
