import json

from django.http import HttpResponse, JsonResponse
from rest_framework import generics, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView

from .models import Eventos, Cia, Empleados, Areas
from .serializers import Eventos_serializer, Cias_serializer, Empleados_serializer, Areas_serializer
from rest_framework.permissions import AllowAny
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate


class RegistrarUsuario(generics.CreateAPIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        usuario = request.data['username']
        email = request.data['email']
        contraseña = request.data['contraseña']
        nombre = request.data['nombre']
        apellido = request.data['apellido']
        staff = request.data['staff']
        nuevo_usuario = User.objects.create_user(usuario, email, contraseña)
        nuevo_usuario.first_name = nombre
        nuevo_usuario.last_name = apellido
        nuevo_usuario.is_staff = staff
        nuevo_usuario.save()
        key_usuario = Token.objects.create(user=nuevo_usuario)
        data = {'detail': 'Usuario se creo Correctamente' + key_usuario.key}
        rpta = json.dumps(data)
        return HttpResponse(rpta, content_type="application/json")


class Loginusuario(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        user = request.data['username']
        contraseña = request.data['password']
        usuario = authenticate(username=user, password=contraseña)
        if usuario:
            key_usuario = Token.objects.get(user_id=usuario.id)
            data = {
                "nombre": usuario.first_name,
                "apellido": usuario.last_name,
                "correo": usuario.email,
                "key": key_usuario.key}
        else:
            data = {"error": "Credenciales Invalidad"}
        rpta = json.dumps(data)
        return HttpResponse(rpta, content_type="application/json")


# todo este servicio me permitira trabajar con el modelo Eventos
@api_view(['GET', 'POST', 'DELETE'])
@permission_classes([AllowAny])
def eventosfull(request):
    if request.method == 'GET':
        eventos = Eventos.objects.all()
        evento = request.GET.get('evento_nombre', None)
        if evento is not None:
            # todo select * from eventos like '%autoriz%'
            eventos = eventos.filter(evento_descripcion__icontains=evento)

    elif request.method == 'POST':
        eventos_data = JSONParser().parse(request)
        eventoserializer = Eventos_serializer(data=eventos_data)
        if eventoserializer.is_valid():
            eventoserializer.save()
            return JsonResponse(eventoserializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(eventoserializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        eventos = Eventos.objects.all().delete()
        return JsonResponse({'Message': '{} Cant Eventos eliminados'.format(eventos[0])},
                            status=status.HTTP_204_NO_CONTENT)

    eventos_serializer = Eventos_serializer(eventos, many=True)
    return JsonResponse(eventos_serializer.data, safe=False)


@api_view(['GET', 'DELETE', 'PUT'])
@permission_classes([AllowAny])
def eventosdetail(request, pk):
    try:
        evento = Eventos.objects.get(eventos_id=pk)
        if request.method == 'GET':
            eventos_serializer = Eventos_serializer(evento)
            return JsonResponse(eventos_serializer.data)
        elif request.method == 'DELETE':
            evento.delete()
            return JsonResponse({'message': 'evento eliminado correctamente'}, status=status.HTTP_204_NO_CONTENT)
        elif request.method == 'PUT':
            eventos_data = JSONParser().parse(request)
            eventoserializer = Eventos_serializer(evento, data=eventos_data)
            if eventoserializer.is_valid():
                eventoserializer.save()
                return JsonResponse(eventoserializer.data)
            return JsonResponse(eventoserializer.errors, status=status.HTTP_400_BAD_REQUEST)


    except Eventos.DoesNotExist:
        return JsonResponse({'message': 'El Codigo del Evento Not Found'}, status=status.HTTP_404_NOT_FOUND)


@api_view(['GET', 'POST', 'DELETE'])
@permission_classes([AllowAny])
def ciasfull(request):
    if request.method == 'GET':
        cias = Cia.objects.all()
    cias_serializer = Cias_serializer(cias, many=True)
    return JsonResponse(cias_serializer.data, safe=False)


@api_view(['GET', 'POST', 'DELETE'])
@permission_classes([AllowAny])
def areasfull(request):
    if request.method == 'GET':
        areas = Areas.objects.all()
    areas_serializer = Areas_serializer(areas, many=True)
    return JsonResponse(areas_serializer.data, safe=False)


@api_view(['GET', 'POST', 'DELETE'])
@permission_classes([AllowAny])
def empleadosfull(request):
    if request.method == 'GET':
        empleados = Empleados.objects.all()
    empleados_serializer = Empleados_serializer(empleados, many=True)
    return JsonResponse(empleados_serializer.data, safe=False)
