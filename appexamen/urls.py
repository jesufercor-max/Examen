from django.urls import path, re_path
from .import views

urlpatterns = [
    path('', views.index , name='index'),
    path('mostrar_videojuegos/', views.mostrar_videojuegos, name='mostrar_videojuegos')
]