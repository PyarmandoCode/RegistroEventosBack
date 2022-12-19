from django.urls import path, include
from . import views
from rest_framework import routers
from .views import RegistrarUsuario,Loginusuario,eventosfull,eventosdetail

router = routers.DefaultRouter()
router.register('full_customers', views.CustomerFull)

urlpatterns = [
    path('api/List_All_Customer', views.CustomerAllViewSet.as_view()),
    # todo http://127.0.0.1:8000/api/List_All_Customer
    path('api/Create_Customer', views.CustomerCreate.as_view()),  # todo http://127.0.0.1:8000/api/Create_Customer
    path('api/Delete_Customer/<customer_id>', views.CustomerDelete.as_view()),
    # todo http://127.0.0.1:8000/api/Delete_Customer
    path('api/Update_Customer/<customer_id>', views.CustomerUpdate.as_view()),
    # todo http://127.0.0.1:8000/api/Update_Customer
    path('api/registro_usuarios',RegistrarUsuario.as_view()),
    path('api/login',Loginusuario.as_view()),
    path('apis/', include(router.urls)),
    path('api/eventosfull',eventosfull),
    path('api/eventosdetail/<pk>',eventosdetail)

]
