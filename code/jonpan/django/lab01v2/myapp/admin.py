from django.contrib import admin
from .models import Priority, TodoItem

admin.site.register([Priority, TodoItem])
