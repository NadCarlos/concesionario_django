from django.urls import path

from autos.views.cars.cars import (
    CarDetail,
    CarList,
    CarCreate,
    Unkwnown,
    CarUpdate,
    CarDelete,
)


from autos.views.cars.cars_reviews import(
    CarReviewView,
    CarReviewCreateView,
    CarReviewUpdateView,
    CarReviewDelete,
)


urlpatterns = [
    path(route='',view=CarList.as_view(), name='car_list'),
    path(route='<int:id>/car_detail/',view=CarDetail.as_view(), name='car_detail'),
    path(route='car_create/',view=CarCreate.as_view(), name='car_create'),
    path(route='<int:id>/car_update/',view=CarUpdate.as_view(), name='car_update'),
    path(route='<int:id>/car_delete/',view=CarDelete.as_view(), name='car_delete'),
    path(route="car_reviews/", view=CarReviewView.as_view(), name="car_reviews"),
    path(route="regatta/", view=Unkwnown.as_view(), name="regatta"),
    path(route="<int:id>/car_create_review/", view=CarReviewCreateView.as_view(), name="car_create_review"),
    path(route="<int:id>/car_update_review/", view=CarReviewUpdateView.as_view(), name="car_update_review"),
    path(route="<int:id>/car_review_delete/", view=CarReviewDelete.as_view(), name="car_review_delete"),
]