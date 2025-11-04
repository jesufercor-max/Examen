from django.conf import settings
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


# Módelo Videojuego
class Videojuego (models.Model):
    id = models.IntegerField(primary_key=True)
    titulo = models.CharField(max_length=50)
    estudio_desarrollo_id = models.IntegerField(unique=True)

# Módelo Sede del estudio
class Sede (models.Model):
    pais = models.CharField(max_length=50)
    videojuego = models.ForeignKey(Videojuego, on_delete = models.CASCADE, null=True) # Relación ManyToOne

# Módelo Estudio
class Estudio (models.Model):
    id = models.IntegerField(primary_key=True)
    sede = models.ForeignKey(Sede, on_delete = models.CASCADE) # Relación ManyToOne
    videojuego = models.ForeignKey(Videojuego, on_delete = models.CASCADE) # Relación ManyToOne

# Módelo Plataformas del videojuego
class Plataforma (models.Model):
    videojuego = models.ManyToManyField(Videojuego, through='videojuego_plataformas') # Relación ManyToMany
    id = models.IntegerField(primary_key=True)

# Módelo Plataformas del videojuego (Tabla intermedia de videojuegos y plataforma)
class videojuego_plataformas (models.Model):
    id = models.IntegerField(primary_key=True)
    videojuego = models.ForeignKey(Videojuego, on_delete = models.CASCADE) # Clave foranea de videojuego
    plataforma = models.ForeignKey(Plataforma, on_delete = models.CASCADE) # Clave foranea de plataforma



