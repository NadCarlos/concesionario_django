from typing import List, Optional

from django.contrib.auth.models import User
from usuarios.models import StandardUser


class StandardUserRepository:

    def get_all(self) -> List[StandardUser]:
        return StandardUser.objects.all()
    
    def filter_by_id(self) -> Optional[StandardUser]:
        return StandardUser.objects.filter(id=id).first()
    
    def get_by_id(self, id: int) -> Optional[StandardUser]:
        try:
            user = StandardUser.objects.get(id=id)
        except:
            user = None
        return user
    
class UserRepository:

    def get_all(self) -> List[User]:
        return User.objects.all()
    
    def filter_by_id(self) -> Optional[User]:
        return User.objects.filter(id=id).first()
    
    def get_by_id(self, id: int) -> Optional[User]:
        try:
            user = User.objects.get(id=id)
        except:
            user = None
        return user