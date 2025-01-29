from sqlalchemy.orm import Mapped

from .base import Base
from .mixins.id_int_pk import IdIntPkMixin

class Product(Base, IdIntPkMixin):
    name: Mapped[str]