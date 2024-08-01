from typing import List, Optional

from autos.models import Brand


class BrandRepository:

    def get_all(self) -> List[Brand]:
        return Brand.objects.all()
    
    def filter_by_id(self) -> Optional[Brand]:
        return Brand.objects.filter(id=id).first()
    
    def get_by_id(self, id: int) -> Optional[Brand]:
        try:
            br = Brand.objects.get(id=id)
        except:
            br = None
        return br