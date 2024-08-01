from typing import List, Optional

from autos.models import CarImage


class CarImageRepository:

    def get_all(self) -> List[CarImage]:
        return CarImage.objects.all()
    
    def filter_by_id(self) -> Optional[CarImage]:
        return CarImage.objects.filter(id=id).first()
    
    def get_by_id(self, id: int) -> Optional[CarImage]:
        try:
            i = CarImage.objects.get(id=id)
        except:
            i = None
        return i