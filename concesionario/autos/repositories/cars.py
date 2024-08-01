from typing import List, Optional

from autos.models import Car, Category, Country, Brand, CarImage


class CarRepository:

    def get_all(self) -> List[Car]:
        return Car.objects.all()
    
    def filter_by_id(self) -> Optional[Car]:
        return Car.objects.filter(id=id).first()
    
    def get_by_id(self, id: int) -> Optional[Car]:
        try:
            car = Car.objects.get(id=id)
        except:
            car = None
        return car
    
    def delete(self, car: Car):
        return car.delete()
    
    def create(
        self,
        name: str,
        price: float,
        brand: Optional[Brand] = None,
        paisOrigen: Optional[Country] = None,
        description: Optional[str] = None,
        stock: Optional[int] = 0,
        category: Optional[Category] = None,
        image: Optional[CarImage] = None,
        
    ):
        return Car.objects.create(
            name=name,
            brand=brand,
            price=price,
            description=description,
            stock=stock,
            category=category,
            paisOrigen=paisOrigen,
            image=image,
        )
    
    def update(
        self, 
        car: Car,
        name: str,
        brand: Brand,
        description: str,
        price: float,
        stock: int,
        category: Category,
        paisOrigen: Country,
        
    ) -> Car:
        if int(stock) < 0:
            raise ValueError("No se pueden ingresar numeros negativos")

        car.name = name
        car.brand = brand
        car.description = description
        car.price = price
        car.stock = stock
        car.category = category
        car.paisOrigen = paisOrigen

        car.save()