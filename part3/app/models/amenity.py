from app import db
from app.models.base import BaseModel
from sqlalchemy.orm import validates


class Amenity(BaseModel):
    __tablename__ = "amenities"

    name = db.Column("name", db.String(50), nullable=False)

    @validates("name")
    def validate_name(self, key, name):
        if not name.strip():
            raise ValueError("Name cannot be empty")

        if len(name) > 50:
            raise ValueError("Name has a maximum length of 50 characters")

        return name

    def as_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
        }
