import re

import flask_bcrypt as bcrypt
from app.models.base import BaseModel


class User(BaseModel):
    _emails = set()
    _email_regex = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,7}"

    def __init__(
        self, first_name: str, last_name: str, email: str, password: str, is_admin=False
    ):
        super().__init__()
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.is_admin = is_admin
        self.password = password
        self.places = []  # users can have many places
        self.amenities = []  # users can have many amenities

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        if len(first_name) > 50:
            raise ValueError("First name has a maximum length of 50 characters")

        if not first_name.strip():
            raise ValueError("First name cannot be empty")

        self._first_name = first_name

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        if len(last_name) > 50:
            raise ValueError("Last name has a maximum length of 50 characters")

        if not last_name.strip():
            raise ValueError("Last name cannot be empty")

        self._last_name = last_name

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        if not re.match(self._email_regex, email) or not email.strip():
            raise ValueError("Not a valid email")

        if email in User._emails:
            raise ValueError("Email is already in use")

        self._email = email

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, password):
        """Set password using hash_password"""
        self.hash_password(password)

    def hash_password(self, password):
        """Hashes the password before storing it."""
        self._password = bcrypt.generate_password_hash(password).decode("utf-8")

    def verify_password(self, password):
        """Verifies if the provided password matches the hashed password."""
        return bcrypt.check_password_hash(self.password, password)

    def add_place(self, place):
        self.places.append(place)

    def add_amenities(self, amenity):
        self.amenities.append(amenity)

    def as_dict(self):
        return {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email,
        }
