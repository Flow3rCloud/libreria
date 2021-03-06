from django.urls import path
from . import views
from django.contrib.staticfiles.urls import static
from django.conf import settings

urlpatterns = [
    path('', views.index, name='inicio'),
    path('donde_estamos/', views.donde_estamos, name='donde_estamos'),
    path('libros/catalogo/', views.catalogo, name='catalogo'),
    path('libros/crear/', views.crear, name='crear_libro'),
    path('libros/editar/<int:id_libro>', views.editar, name='editar_libro'),
    path('libros/eliminar/<int:id_libro>', views.eliminar, name='eliminar_libro'),
    path('libros/gestion/', views.gestion, name='gestion_catalogo'),
    path('libros/test/', views.test, name='test'),
    path('libros/catalogo_json/', views.catalogo_json, name='catalogo_json'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


