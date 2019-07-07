from django.urls import path
from core import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('data-tables/', views.hovertable, name='data-tables'),
    path('modals/', views.modal, name='modals'),
]