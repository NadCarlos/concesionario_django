from django.shortcuts import render
from django.views import View

from django.utils.translation import activate

from usuarios.models import StandardUser

class IndexView(View):

    def get(self, request, *args, **kwargs):
        if not request.user.is_anonymous:
            profile = StandardUser.objects.get(user=request.user)
            lang = profile.language
            print(lang)
            activate(lang)
        return render(
            request,
            'home/index.html'
        )