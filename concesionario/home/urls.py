from django.urls import path

from home.views.index import IndexView
from home.views.error import ErrorView


urlpatterns = [
    path(route='',view=IndexView.as_view(), name='index'),
    path(route='error/',view=ErrorView.as_view(), name='error'),
]