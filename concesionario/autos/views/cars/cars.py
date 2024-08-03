from django.views import View
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render, redirect

from autos.forms import (
    CarForm,
    CarUpdateForm
    )

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


class CarCreate(View):
    
    @method_decorator(permission_required(perm='concesionario.car_create', login_url='login', raise_exception=True))
    @method_decorator(login_required(login_url='login'))
    def get(self, request):
        form = CarForm(request.POST)
        return render(
            request,
            'cars/create.html',
            dict(
                form=form
            )
        )
    
    @method_decorator(permission_required(perm='concesionario.car_create', login_url='login', raise_exception=True))
    @method_decorator(login_required(login_url='login'))
    def post(self, request):
        form = CarForm(request.POST)
        if form.is_valid():
            new_car = carRepo.create(
                name=form.cleaned_data['name'],
                brand=form.cleaned_data['brand'],
                description=form.cleaned_data['description'],
                price=form.cleaned_data['price'],
                stock=form.cleaned_data['stock'],
                category=form.cleaned_data['category'],
                paisOrigen=form.cleaned_data['paisOrigen'],
                image=form.cleaned_data['image'],
                )
            return redirect('car_detail', new_car.id)
        

class CarUpdate(View):

    @method_decorator(permission_required(perm='concesionario.car_create', login_url='login', raise_exception=True))
    @method_decorator(login_required(login_url='login'))
    def get(self, request, id):
        car = carRepo.get_by_id(id=id)
        form = CarUpdateForm(instance=car)
        return render(
            request,
            'cars/update.html',
            dict(
                form=form,
            )
        )
    
    @method_decorator(permission_required(perm='concesionario.car_create', login_url='login', raise_exception=True))
    @method_decorator(login_required(login_url='login'))
    def post(self, request, id):
        car = carRepo.get_by_id(id=id)

        description = request.POST.get('description')
        price = request.POST.get('price')
        stock = request.POST.get('stock')

        car.description = description
        car.price = price
        car.stock = stock

        car.save()

        return redirect('car_list')
    

class CarDelete(View):

    @method_decorator(permission_required(perm='concesionario.car_create', login_url='login', raise_exception=True))
    @method_decorator(login_required(login_url='login'))
    def get(self, request, id):
        car = carRepo.get_by_id(id=id)
        carRepo.delete(car=car)
        return redirect('car_list')
