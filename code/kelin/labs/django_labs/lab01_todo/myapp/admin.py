# from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Priority, ToDoItem

admin.site.register(Priority)
admin.site.register(ToDoItem) # Registered Priority and ToDoItem models