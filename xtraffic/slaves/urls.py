from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_slave, name='add_slave'),
    path('', views.slave_list, name='slave_list')  
]
