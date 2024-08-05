from django.db import models
from django.contrib.auth.models import User


class CarImage(models.Model):
    image = models.ImageField(upload_to='car_images/')
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.description


class Category(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return  self.name
    

class Country(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return  self.name


class Brand(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return  self.name


class Car(models.Model):
    name = models.CharField(max_length=100)

    brand = models.ForeignKey(
        Brand,
        on_delete=models.SET_NULL,
        related_name='cars',
        null=True,
    )

    description = models.TextField(
        null=True,
        blank=True,
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
    )
    stock = models.IntegerField(default=0)
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        related_name='cars',
        null=True,
    )
    paisOrigen = models.ForeignKey(
        Country,
        on_delete=models.SET_NULL,
        related_name='cars',
        null=True,
    )

    image = models.ForeignKey(
        CarImage,
        on_delete=models.SET_NULL,
        related_name='cars',
        null=True,
    )


    def __str__(self):
        return  self.name
    

class Rating(models.Model):
    rating = models.IntegerField()

    def __str__(self):
        string=str(self.rating)
        return string


class CarReview(models.Model):
    car = models.ForeignKey(
        Car,
        on_delete=models.CASCADE,
        related_name='reviews',
    )
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    date = models.DateField(auto_now_add=True)
    rating = models.ForeignKey(
        Rating,
        on_delete=models.CASCADE,
        related_name='reviews',
    )

    def __str__(self):
        return f'Review by {self.author.username} for {self.car.name}'
