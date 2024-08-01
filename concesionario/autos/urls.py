from django.urls import path

from autos.views.cars.cars import (
    CarDetail,
    CarList,
)


urlpatterns = [
    path(route='',view=CarList.as_view(), name='car_list'),
    path(route='<int:id>/car_detail',view=CarDetail.as_view(), name='car_detail'),
]