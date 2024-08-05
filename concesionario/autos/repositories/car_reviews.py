from typing import List, Optional

from autos.models import CarReview, Car, Rating
from django.contrib.auth.models import User

from autos.repositories.cars import CarRepository

class CarReviewRepository:
    def get_all(self) -> List[CarReview]:
        return CarReview.objects.all()
    
    def filter_by_id(self) -> Optional[CarReview]:
        return CarReview.objects.filter(id=id).all()
    
    def get_by_id(self, id: int) -> Optional[CarReview]:
        try:
            car_review = CarReview.objects.get(id=id)
        except:
            car_review = None
        return car_review
    
    def delete(self, car_review: CarReview):
        return car_review.delete()
    
    
    def create(
        self,
        car: Car,
        author: User,
        text: str,
        rating: Rating,
        *args, 
        **kwargs,
    ) -> CarReview:

        review = CarReview.objects.create(
            car=car,
            author=author,
            text=text,
            rating=rating,
        )
        return review
    
    def update(
        self,
        car: Car,
        author: User,
        text: str,
        rating: Rating,
        *args, 
        **kwargs,
    ) -> CarReview:

        review = CarReview.objects.update(
            car=car,
            author=author,
            text=text,
            rating=rating,
        )
        return review