from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('informatica.urls')),  # Asegúrate de incluir las URLs de la app
]
