from msilib import CAB
from django.contrib import admin

from .models import Todolist, Category

# Register your models here.

admin.site.register(Todolist)
admin.site.register(Category)