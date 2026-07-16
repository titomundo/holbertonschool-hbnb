from app import db
from app.models.base import BaseModel
from sqlalchemy import ForeignKey
from sqlalchemy.orm import validates


class Review(BaseModel):
    __tablename__ = "reviews"

    text = db.Column("text", db.String(1024), nullable=True)
    rating = db.Column("rating", db.Integer, nullable=False)
    place_id = db.Column("place_id", db.String(36), ForeignKey("places.id"), nullable=False)
    user_id = db.Column("user_id", db.String(36), ForeignKey("users.id"), nullable=False)

    @validates("text")
    def validate_text(self, key, text):
        if not text.strip():
            raise ValueError("Text cannot be empty")

        return text

    @validates("rating")
    def validate_rating(self, key, rating):
        if 1 > rating or rating > 5:
            raise ValueError("range must be between 1 and 5")

        return rating

    def as_dict(self):
        return {
            "id": self.id,
            "text": self.text,
            "rating": self.rating,
            "place_id": self.place_id,
            "user_id": self.user_id,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
        }
