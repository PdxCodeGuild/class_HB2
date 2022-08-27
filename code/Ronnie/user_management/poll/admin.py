from django.contrib import admin
from .models import Question, Choice, User
from django.contrib.auth.admin import UserAdmin
# Register your models here.

admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(User, UserAdmin)