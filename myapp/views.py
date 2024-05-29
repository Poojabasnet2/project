from django.shortcuts import render
from django.views.generic import ListView ,CreateView 
from .models import *
from django.views import View
from .forms import MenuForm
from django.urls import reverse_lazy

class MenuList(ListView):
    model=Menu
    context_object_name='list'
    template_name="menu.html"

class AddItem(CreateView):
    model=Menu
    form_class=MenuForm
    template_name="add_item.html"
    success_url = reverse_lazy('menu')

