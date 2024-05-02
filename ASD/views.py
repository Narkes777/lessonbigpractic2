from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Todolist

# Create your views here.

class TodoList(ListView):
    model = Todolist
    context_object_name = 'todo_list'
    paginate_by = 1

class TodolistDetail(DetailView):
    model = Todolist
    context_object_name = 'todo'

class TodolistCreate(CreateView):
    model = Todolist
    fields = '__all__'
    success_url = reverse_lazy('todo_list')

class TodolistUpdate(UpdateView):
    model = Todolist
    fields = '__all__'
    success_url = reverse_lazy('todo_list')

class TodolistDelete(DeleteView):
    model = Todolist
    fields = '__all__'
    success_url = reverse_lazy('todo_list')
    template_name = 'ASD/todolist_form.html'