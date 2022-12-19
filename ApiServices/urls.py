from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Backend.urls')), #todo http://127.0.0.1:8000/back/api/eventosfull
    
]
