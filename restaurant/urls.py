from django.contrib import admin 
from django.urls import path

from . import views

urlpatterns = [ 
    path('menu/', views.MenuItemsView.as_view(), name='index'),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view(), name='menu_view'),

]