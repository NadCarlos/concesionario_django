from django.views import View
from django.shortcuts import redirect, render
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required, permission_required

from autos.repositories.cars import CarRepository
from autos.repositories.car_reviews import CarReviewRepository
from autos.repositories.rating import RatingRepository

from autos.forms import CarReviewForm


carRepo = CarRepository()
reviewsRepo = CarReviewRepository()
ratingRepo = RatingRepository()


class CarReviewView(View):
    def get(self, request):
        reviews = reviewsRepo.get_all()
        return render(
            request,
            'car_reviews/list.html',
            dict(
                reviews=reviews
            )
        )

class CarReviewCreateView(View):

    @method_decorator(login_required(login_url='login'))
    def get(self, request, id):
        car = carRepo.get_by_id(id=id)
        form = CarReviewForm(initial = {'car': car, 'author': request.user})
        return render(
            request,
            'car_reviews/create.html',
            dict(
                form=form,
                car=car,
            )
        )
    
    @method_decorator(login_required(login_url='login'))
    def post(self, request, id, *args, **kwargs):
        form = CarReviewForm(request.POST)
        if form.is_valid():
            reviewsRepo.create(
                car=form.cleaned_data['car'],
                author=form.cleaned_data['author'],
                text=form.cleaned_data['text'],
                rating=form.cleaned_data['rating'],
                )
            return redirect('car_reviews')
        else:
            return redirect('error')


class CarReviewUpdateView(View):

    @method_decorator(login_required(login_url='login'))
    def get(self, request, id):
        review = reviewsRepo.get_by_id(id=id)
        form = CarReviewForm(instance=review)
        if request.user.id == review.author.id:
            return render(
                request,
                'car_reviews/update.html',
                dict(
                    form=form,
                )
            )
        else:
            return redirect('error')
    
    @method_decorator(login_required(login_url='login'))
    def post(self, request, id, *args, **kwargs):
        form = CarReviewForm(request.POST)
        if form.is_valid():
            reviewsRepo.update(
                car=form.cleaned_data['car'],
                author=form.cleaned_data['author'],
                text=form.cleaned_data['text'],
                rating=form.cleaned_data['rating'],
                )
            return redirect('car_reviews')
        else:
            return redirect('error')


class CarReviewDelete(View):

    @method_decorator(login_required(login_url='login'))
    def get(self, request, id):
        review = reviewsRepo.get_by_id(id=id)
        if request.user.id == review.author.id or request.user.is_staff:
            reviewsRepo.delete(review)
            return redirect('car_reviews')
        else:
            return redirect('error')
