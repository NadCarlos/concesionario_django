from django.db import models
from django.contrib.auth.models import User

from autos.models import Country


class Province(models.Model):
    name = models.CharField(max_length=200)

    pais = models.ForeignKey(
        Country,
        on_delete=models.CASCADE,
        related_name='localidad',
    )

    def __str__(self):
        return  self.name


class Location(models.Model):
    name = models.CharField(max_length=200)

    provincia = models.ForeignKey(
        Province,
        on_delete=models.CASCADE,
        related_name='localidad',
    )

    def __str__(self):
        return  self.name

class StandardUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    localidad = models.ForeignKey(
        Location,
        on_delete=models.CASCADE,
        related_name='standardUser',
    )
    
    def __str__(self):
        return  self.user.username
