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
        if len(title) > 100:
            raise ValueError("title has a maximum length of 100 characters")

        if price < 0:
            raise ValueError("price must be a positive value")

        if -90.0 > latitude or latitude > 90.0:
            raise ValueError("latitude range must be between -90.0 and 90.0")

        if -180.0 > longitude or longitude > 180.0:
            raise ValueError("longitude range must be between -180.0 and 180.0")

        super().__init__()
        self.title = title
        self.description = description
        self.price = price
        self.latitude = latitude
        self.longitude = longitude
        self.owner_id = owner_id
        self.reviews = []  # places can have multiple reviews
        self.amenities = amenities

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
