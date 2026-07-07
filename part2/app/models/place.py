from app.models.base import BaseModel
from app.models.user import User


class Place(BaseModel):
    def __init__(
        self,
        title: str,
        price: float,
        owner_id: User,
        latitude: float,
        longitude: float,
        description: str = "",
        amenities=[],
    ):
        super().__init__()
        self.title = title
        self.description = description
        self.price = price
        self.latitude = latitude
        self.longitude = longitude
        self.owner_id = owner_id
        self.reviews = []  # places can have multiple reviews
        self.amenities = amenities

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        if len(title) > 100:
            raise ValueError("Title has a maximum length of 100 characters")

        if not title.strip():
            raise ValueError("Title cannot be empty")

        self._title = title

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, description):
        self._description = description

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, price):
        if price < 0:
            raise ValueError("Price must be a positive number")

        self._price = price

    @property
    def latitude(self):
        return self._latitude

    @latitude.setter
    def latitude(self, latitude):
        if -90.0 > latitude or latitude > 90.0:
            raise ValueError("Latitude range must be between -90.0 and 90.0")

        self._latitude = latitude

    @property
    def longitude(self):
        return self._longitude

    @longitude.setter
    def longitude(self, longitude):
        if -180.0 > longitude or longitude > 180.0:
            raise ValueError("Longitude range must be between -180.0 and 180.0")

        self._longitude = longitude

    def add_review(self, review):
        self.reviews.append(review)

    def add_amenity(self, amenity):
        self.amenities.append(amenity)

    def as_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "price": self.price,
            "latitude": self.latitude,
            "longitude": self.longitude,
            "owner_id": self.owner_id,
        }
