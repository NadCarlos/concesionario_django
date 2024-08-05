from typing import List, Optional

from autos.models import Rating


class RatingRepository:

    def get_all(self) -> List[Rating]:
        return Rating.objects.all()
    
    def filter_by_id(self) -> Optional[Rating]:
        return Rating.objects.filter(id=id).first()
    
    def get_by_id(self, id: int) -> Optional[Rating]:
        try:
            r = Rating.objects.get(id=id)
        except:
            r = None
        return r