from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('drugs/', views.page1, name='drugs'),
    path('slaves/', views.page2, name='slaves'),
    path('guns/', views.page3, name='guns'),
    path('prostitutes/', views.page4, name='prostitutes'),
]
