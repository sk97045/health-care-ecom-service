class Product:
    _id: str | None 
    name: str | None 
    category: str | None
    price: float | None
    units_available: int | None


    def __init__(self, _id: str = None,
                 name: str = None,
                 category: str = None,
                 price: str = None,
                 units_available: str = None):
        self._id = _id
        self.name = name
        self.category = category
        self.price = price
        self.units_available = units_available