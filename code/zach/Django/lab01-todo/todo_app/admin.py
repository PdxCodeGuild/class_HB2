from django.contrib import admin
from .models import Priority, ToDoItem

# Register your models here.
admin.site.register(Priority)
admin.site.register(ToDoItem)