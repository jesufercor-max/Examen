from django.shortcuts import render
from .models import *
from django.db.models import Avg, Max, Min, Q, Prefetch, F
from django.views.defaults import page_not_found


# Create your views here.

# Vista Index
def index(request):
    return render(request, 'index.html') 

# Vista 1: Mostrar datos de los videojuegos
def mostrar_videojuegos (request):
    """
    SELECT V.*,E.*,VP.*,P.*
    FROM videojuego V
    INNER JOIN estudio E ON V.estudio_desarrollo_id = E.id
    INNER JOIN sede S ON E.id = S.estudio_id
    LEFT JOIN videojuego_plataformas VP ON V.id = VP.videojuego_id
    LEFT JOIN plataforma P ON VP.plataforma_id = P.id
    LEFT JOIN analisis A ON V.id = A.videojuego_id
    WHERE V.titulo LIKE '%Fantasy%' AND S.pais LIKE '%Unidos%';
    """
    videojuegos = Videojuego.objects.all()
    videojuegos = Videojuego.objects.select_related("estudio", "sede").prefetch_related("plataforma")
    Videojuego.objects.filter (videojuego_titulo__contains =F("Fantasy") , sede_pais__contains = ("Unidos"))
    return render (request, 'appexamen/mostrar_videojuegos.html', {"mostrar_videojuegos":videojuegos})

#   PÁGINAS DE ERRORES
def mi_error_404(request, exception=None):
    return render(request, 'Errores/404.html',None,None,404)

def mi_error_400(request, exception=None):
    return render(request, 'Errores/400.html',None,None,400)

def mi_error_403(request, exception=None):
    return render(request, 'Errores/403.html',None,None,403)

def mi_error_500(request, exception=None):
    return render(request, 'Errores/500.html',None,None,500)