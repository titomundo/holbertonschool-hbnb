from app.models.base import BaseModel
from app.models.user import User


class Place(BaseModel):

    def __init__(
        self,
        title: str,
        price: float,
        owner: User,
        latitude: float = None,
        longitude: float = None,
        description: str= "",
    ):
        if len(title) > 100:
            raise ValueError("title has a maximum length of 100 characters")

        if price < 0:
            raise ValueError("price must be a positive value")

        if latitude is not None and (-90.0 > latitude or latitude > 90.0):
            raise ValueError("latitude range must be between -90.0 and 90.0")

        if longitude is not None and (-180.0 > longitude or longitude > 180.0):
            raise ValueError("longitude range must be between -180.0 and 180.0")

        super().__init__()
        self.title = title
        self.description = description
        self.price = price
        self.latitude = latitude
        self.longitude = longitude
        self.owner = owner
        self.reviews = [] # places can have multiple reviews

    def add_review(self, review):
        self.reviews.append(review)
