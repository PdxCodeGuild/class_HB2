from rest_framework.routers import DefaultRouter
from django.urls import path
from .views import ToDoViewSet

router = DefaultRouter()
router.register('todo', ToDoViewSet, basename='ToDo')

urlpatterns = router.urls + [

]