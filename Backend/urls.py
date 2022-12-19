from django.urls import path

from .views import RegistrarUsuario, Loginusuario, eventosfull, eventosdetail, ciasfull, areasfull, empleadosfull

urlpatterns = [

    # todo http://127.0.0.1:8000/api/Update_Customer
    path('api/registro_usuarios', RegistrarUsuario.as_view()),
    path('api/login', Loginusuario.as_view()),
    path('api/eventosfull', eventosfull),
    path('api/ciasfull', ciasfull),
    path('api/empleadosfull', empleadosfull),
    path('api/areasfull', areasfull),
    path('api/eventosdetail/<pk>', eventosdetail)

]
