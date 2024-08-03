from django.contrib.auth import (
    login,
)

from django.shortcuts import redirect, render
from django.views import View
from usuarios.forms import LoginForm


class LoginView(View):

    form_class = LoginForm
    template_name = 'users/login.html'

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
        form = self.form_class(request.POST or None)
        if request.POST and form.is_valid():
            user = form.login(request)
            if user:
                login(request, user)
                return redirect ('index')
        return render(
            request,
            self.template_name,
            dict(
                form=form,
            )
        )