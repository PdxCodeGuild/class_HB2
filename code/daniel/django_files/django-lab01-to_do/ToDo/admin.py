from django.contrib import admin
from .models import MyModel, ToDoItem, Priority

admin.site.register(MyModel)
admin.site.register(ToDoItem)
admin.site.register(Priority)
