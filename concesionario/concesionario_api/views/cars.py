from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from autos.models import Car, Category, CarReview
from usuarios.models import User

from concesionario_api.serializers.cars import (
    CarSerializer,
    CarReviewSerializer,
    UserSerializer,
)


class CarApiView(APIView):

    def get(self, request, *args, **kwargs):
        autos = Car.objects.all()
        serializer = CarSerializer(autos, many=True)
        car_id = self.kwargs.get('pk', None)
        if car_id:
            cars = autos.get(id=car_id)
            serializer = CarSerializer(autos)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ComentariosApiView(APIView):

    def get(self, request, pk, *args, **kwargs):
        comentarios = CarReview.objects.filter(car=pk)
        serializer = CarReviewSerializer(comentarios, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class UserApiView(APIView):

    permission_classes = [IsAuthenticated]
    
    def get(self, request, *args, **kwargs):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)