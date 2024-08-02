from django.urls import path

from autos.views.cars.cars import (
    CarDetail,
    CarList,
    CarCreate,
    CarUpdate,
    CarDelete,
)


urlpatterns = [
    path(route='',view=CarList.as_view(), name='car_list'),
    path(route='<int:id>/car_detail/',view=CarDetail.as_view(), name='car_detail'),
    path(route='car_create/',view=CarCreate.as_view(), name='car_create'),
    path(route='<int:id>/car_update/',view=CarUpdate.as_view(), name='car_update'),
    path(route='<int:id>/car_delete/',view=CarDelete.as_view(), name='car_delete'),
]