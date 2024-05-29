
from django.urls import path
from django.views import *
from .import views
from .views import *



urlpatterns = [
    path('menu',views.MenuList.as_view(),name='menu'),
    path('add_item',views.AddItem.as_view(),name='add_item'),
]
