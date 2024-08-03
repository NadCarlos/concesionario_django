from django.urls import path

from usuarios.views.register import RegisterView
from usuarios.views.login import LoginView
from usuarios.views.logout import LogoutView
from usuarios.views.profile import ProfileView
from usuarios.views.profile import ProfileUpdate


urlpatterns = [
    path(route='register/', view=RegisterView.as_view(), name='register'),
    path(route='login/', view=LoginView.as_view(), name='login'),
    path(route='logout/', view=LogoutView.as_view(), name='logout'),
    path(route='<int:id>/profile/', view=ProfileView.as_view(), name='profile'),
    path(route='<int:id>/profile_update/', view=ProfileUpdate.as_view(), name='profile_update'),
]