from typing import List, Optional

from autos.models import Country


class CountryRepository:

    def get_all(self) -> List[Country]:
        return Country.objects.all()
    
    def filter_by_id(self) -> Optional[Country]:
        return Country.objects.filter(id=id).first()
    
    def get_by_id(self, id: int) -> Optional[Country]:
        try:
            c = Country.objects.get(id=id)
        except:
            c = None
        return c