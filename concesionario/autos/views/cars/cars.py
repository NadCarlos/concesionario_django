from django.views import View
from django.shortcuts import render

from autos.repositories.cars import CarRepository


carRepo = CarRepository()


class CarList(View):
    def get(self, request):
        cars = carRepo.get_all()
        return render(
            request,
            'cars/list.html',
            dict(
                cars=cars
            )
        )


class CarDetail(View):
    def get(self, request, id):
        car = carRepo.get_by_id(id=id)
        return render(
            request,
            'cars/detail.html',
            dict(
                car=car,
            )
        )
