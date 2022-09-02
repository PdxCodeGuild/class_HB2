from django.contrib import admin


from .models import Priority, Todoitem

admin.site.register([Priority, Todoitem])
