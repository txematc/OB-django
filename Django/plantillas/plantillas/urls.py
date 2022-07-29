from django.contrib import admin
from django.urls import path
# Importamos las views aqui a la url como en el anterior
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('simple/', views.simple, name="simple"),
    path('plantilladinamica/<str:nombreusuario>/',
         views.plantilladinamica, name="plantilladinamica")
]