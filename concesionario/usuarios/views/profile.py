from django.views import View
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from usuarios.repositories.users import (
    UserRepository,
)

from usuarios.forms import ProfileUpdateForm


usersRepo = UserRepository()


class ProfileView(View):

    @method_decorator(login_required(login_url='login'))
    def get(self, request, id, *args, **kwargs):
        usuario = usersRepo.get_by_id(id=id)
        print(usuario)
        return render(
            request,
            'users/profile.html',
            dict(
                usuario=usuario
            )
        )


class ProfileUpdate(View):

    @method_decorator(login_required(login_url='login'))
    def get(self, request, id):
        print(usersRepo)
        user = usersRepo.get_by_id(id=id)
        print(user)
        form = ProfileUpdateForm(instance=user)
        return render(
            request,
            'users/update.html',
            dict(
                form=form,
            )
        )
    
    @method_decorator(login_required(login_url='login'))
    def post(self, request, id):
        user = usersRepo.get_by_id(id=id)

        username = request.POST.get('username')
        email = request.POST.get('email')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')

        user.username = username
        user.email = email
        user.first_name = first_name
        user.last_name = last_name

        user.save()

        return redirect('index')