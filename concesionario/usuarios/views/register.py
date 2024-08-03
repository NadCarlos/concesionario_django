from django.contrib.auth import (
    login,
)

from django.shortcuts import redirect, render
from django.views import View
from usuarios.forms import UserRegisterForm


class RegisterView(View):

    form_class = UserRegisterForm
    template_name = 'users/register.html'

    def get(self, request):
        form = self.form_class()

        return render(
            request,
            self.template_name,
            dict(
                form=form
            )
        )
    
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect ('index')
        
        return render(
            request,
            self.template_name,
            dict(
                form=form
            )
        )