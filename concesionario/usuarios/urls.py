from django.urls import path

from usuarios.views.register import RegisterView
from usuarios.views.login import LoginView


urlpatterns = [
    path(route='register/', view=RegisterView.as_view(), name='register'),
    path(route='login/', view=LoginView.as_view(), name='login'),
]