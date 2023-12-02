from typing import List

from app.modules.user.types.address import Address


class User:
    _id: str = None
    first_name: str = None
    last_name: str = None
    primary_email: str = None
    secondary_email: str = None
    primary_phone_number: str = None
    secondary_phone_number: str = None
    addresses: List[Address] = []
    user_type: str = None

    def __init__(self, _id: str = None,
                 first_name: str = None,
                 last_name: str = None,
                 primary_email: str = None,
                 secondary_email: str = None,
                 primary_phone_number: str = None,
                 secondary_phone_number: str = None,
                 addresses: List[Address] = [],
                 user_type: str = None):
        self._id = _id
        self.first_name = first_name
        self.last_name = last_name
        self.primary_email = primary_email
        self.secondary_email = secondary_email
        self.primary_phone_number = primary_phone_number
        self.secondary_phone_number = secondary_phone_number
        self.addresses = list(map(lambda x: Address(**x), addresses))
        self.user_type = str(user_type)
