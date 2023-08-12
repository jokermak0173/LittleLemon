from django.contrib import admin 
from django.urls import path

from rest_framework.authtoken.views import obtain_auth_token

from . import views

urlpatterns = [ 
    path('menu/', views.MenuItemsView.as_view(), name='index'),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view(), name='menu_view'),
]