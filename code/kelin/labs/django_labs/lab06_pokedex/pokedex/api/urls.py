from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import PokemonViewSet, TypeViewSet, UserView, CurrentUser

router = DefaultRouter()
router.register('pokemon', PokemonViewSet, basename='pokemon')
router.register('type', TypeViewSet, basename='type')
router.register('users', UserView, basename='users')

urlpatterns = router.urls + [
    path('currentuser/', CurrentUser.as_view())
]