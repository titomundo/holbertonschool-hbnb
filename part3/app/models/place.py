from app import db
from app.models.base import BaseModel
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, validates


class Place(BaseModel):
    __tablename__ = "places"

    title = db.Column("title", db.String(100), nullable=False)
    description = db.Column("description", db.String(), default="")
    price = db.Column("price", db.Float, nullable=False)
    latitude = db.Column("latitude", db.Float, nullable=False)
    longitude = db.Column("longitude", db.Float, nullable=False)
    owner_id = db.Column(
        "owner_id", db.String(36), ForeignKey("users.id"), nullable=False
    )

    place_amenity = db.Table(
        "place_amenity",
        db.Column("place_id", db.String(36), ForeignKey("places.id"), primary_key=True),
        db.Column(
            "amenity_id", db.String(36), ForeignKey("amenities.id"), primary_key=True
        ),
    )

    reviews = relationship("Review", backref="place", lazy=True)
    amenities = relationship(
        "Amenity",
        secondary=place_amenity,
        lazy="subquery",
        backref=db.backref("reviews", lazy=True),
    )

    @validates("title")
    def validate_title(self, key, title):
        if len(title) > 100:
            raise ValueError("Title has a maximum length of 100 characters")

        if not title.strip():
            raise ValueError("Title cannot be empty")

        return title

    @validates("price")
    def validate_price(self, key, price):
        if price < 0:
            raise ValueError("Price must be a positive number")

        return price

    @validates("latitude")
    def validate_latitude(self, key, latitude):
        if -90.0 > latitude or latitude > 90.0:
            raise ValueError("Latitude range must be between -90.0 and 90.0")

        return latitude

    @validates("longitude")
    def validate_longitude(self, key, longitude):
        if -180.0 > longitude or longitude > 180.0:
            raise ValueError("Longitude range must be between -180.0 and 180.0")

        return longitude

    def as_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "price": self.price,
            "latitude": self.latitude,
            "longitude": self.longitude,
            "owner_id": self.owner_id,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
        }
