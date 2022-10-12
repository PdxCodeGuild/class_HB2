from rest_framework import routers
from .views import PokemonViewSet, TypeViewSet

router = routers.DefaultRouter()
router.register('pokemon', PokemonViewSet, basename='pokemon')
router.register('types', TypeViewSet, basename='types')

app_name = 'pokeapp'
urlpatterns = router.urls + [
    
]