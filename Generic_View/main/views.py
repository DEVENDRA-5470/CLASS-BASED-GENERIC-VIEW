from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.views.generic.edit import DeleteView
from django.views.generic.edit import UpdateView
from .models import *
from .forms import *
# Create your views here.
class Create_data(CreateView):
    model = Employee
    fields="__all__"

    success_url = '/list'
class List_data(ListView):
    model = Employee

class Delete_data(DeleteView):
    model = Employee
    success_url = '/list'

    
class Update_data(UpdateView):
    model = Employee
    fields="__all__"

    success_url = '/list'

    