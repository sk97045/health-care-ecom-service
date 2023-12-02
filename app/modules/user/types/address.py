class Address:
    address_line_1: str = None
    address_line_2: str = None
    city: str = None
    district: str = None
    state: str = None
    country: str = None
    postal_code: str = None
    is_primary: bool = None

    def __init__(
            self, address_line_1=None, address_line_2=None, city: str = None,
            district: str = None, state: str = None, country: str = None,
            postal_code: str = None, is_primary: bool = None):
        self.address_line_1 = address_line_1
        self.address_line_2 = address_line_2
        self.city = city
        self.district = district
        self.state = state
        self.country = country
        self.postal_code = postal_code
        self.is_primary = is_primary
