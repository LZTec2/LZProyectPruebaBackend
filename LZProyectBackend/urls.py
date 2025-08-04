from django.contrib import admin
from django.urls import path
from core.views import qr_list_create, qr_list_public, qr_list_search, qr_find_by_content

urlpatterns = [
    path('admin/', admin.site.urls), # Admin de Django
    path('api/qr/', qr_list_create, name='qr-list-create'), # Crear y listar todos los QR
    # Guardar un QR (POST): 'api/qr/'
    # Obtener todos los QR (GET): 'api/qr/'
path('api/qr/public/', qr_list_public, name='qr-list-public'), # Obtener solo los QR públicos (GET)
path('api/qr/search/', qr_list_search, name='qr-list-search'), # Buscar QR por texto (nombre, autor o contenido) (GET, parámetro 'q')
path('api/qr/content/<str:content>/', qr_find_by_content, name='qr-find-by-content'), # Buscar un QR por su contenido (GET)
]
