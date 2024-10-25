from rest_framework.routers import path

from concesionario_api.views.cars import (
    CarApiView,
    ComentariosApiView,
    UserApiView
)

urlpatterns = [
    path('car_apiview', CarApiView.as_view(), name='car_apiview'),
    path('car_apiupdate/<int:pk>', CarApiView.as_view(), name='car_apiupdate'),
    path('car_apigetone/<int:pk>', CarApiView.as_view(), name='car_apigetone'),
    path('coment_apiview/<int:pk>', ComentariosApiView.as_view(), name='coment_apiview'),
    path('user_apiview', UserApiView.as_view(), name='user_apiview'),
]