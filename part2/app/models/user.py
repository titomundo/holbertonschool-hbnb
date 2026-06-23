from app.models.base import BaseModel
import re


class User(BaseModel):
    _emails = set()
    _email_regex = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,7}"

    def __init__(
        self, first_name: str, last_name: str, email: str, is_admin=False
    ):
        if len(first_name) > 50:
            raise ValueError("first_name has a maximum length of 50 characters")

        if len(last_name) > 50:
            raise ValueError("last_name has a maximum length of 50 characters")

        if not re.match(self._email_regex, email):
            raise ValueError("Not a valid email")

        if email in User._emails:
            raise ValueError("email is already in use")

        super().__init__()
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.is_admin = is_admin
        self.places = [] # users can have many places
        self.amenities = [] # users can have many amenities

    def add_place(self, place):
        self.places.append(place)

    def add_amenities(self, amenity):
        self.amenities.append(amenity)
