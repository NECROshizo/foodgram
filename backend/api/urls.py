from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import include, path, re_path
from rest_framework import routers
from .views import (
    UserViewSet,
    TagViewSet,
    IngredientsViewSet,
    RecipesViewSet,
)


app_name = 'api'
router = routers.DefaultRouter()
# router.register('users', UserViewSet)
router.register('tags', TagViewSet, basename='tags')
router.register('ingredients', IngredientsViewSet, basename='ingredients')
router.register('recipes', RecipesViewSet, basename='recipes')


urlpatterns = [
    path('', include(router.urls)),
    # path('auth', include('djoser.urls')),
    # path('auth', include('djoser.urls.authtoken')),
    re_path(r'', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
]