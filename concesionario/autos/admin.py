from django.contrib import admin
from autos.models import (
    CarImage,
    Category,
    Country,
    Brand,
    Car,
    Rating,
    CarReview,
)


@admin.register(CarImage)
class CarImageAdmin(admin.ModelAdmin):
    list_display = (
        'image',
    )


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )


@admin.register(CarReview)
class CarReviewAdmin(admin.ModelAdmin):
    list_display = (
        'text',
    )


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = (
        'rating',
    )