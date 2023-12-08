from datetime import datetime

class Product:
    name: str | None 
    category: str | None
    description: str | None
    price: float | None
    units_available: int | None
    created_at: datetime | None
    updated_at: datetime | None


    def __init__(self,
                 name: str = None,
                 category: str = None,
                 description: str = None,
                 price: str = None,
                 units_available: str = None):
        self.name = name
        self.category = category
        self.description = description
        self.price = price
        self.units_available = units_available

    def set_create_time(self, created_at: datetime | None):
        self.created_at = created_at
        self.updated_at = created_at

    def set_update_time(self, updated_at: datetime | None):
        self.updated_at = updated_at