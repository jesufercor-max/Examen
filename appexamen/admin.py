from django.contrib import admin
from .models import Videojuego, Sede, Estudio, Plataforma , videojuego_plataformas 

# Register your models here.

admin.site.register(Videojuego)
admin.site.register(Sede)
admin.site.register(Estudio)
admin.site.register(Plataforma)
admin.site.register(videojuego_plataformas)
