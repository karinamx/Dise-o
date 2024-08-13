from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # Ruta para el panel de administración
    path('', include('myApp.urls')),  # Incluir las rutas de la aplicación 'myApp'
]
