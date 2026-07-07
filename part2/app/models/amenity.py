from app.models.base import BaseModel


class Amenity(BaseModel):
    def __init__(self, name: str):
        if not name.strip():
            raise ValueError("Name cannot be empty")

        if len(name) > 50:
            raise ValueError("Name has a maximum length of 50 characters")

        super().__init__()
        self.name = name

    def as_dict(self):
        return {"id": self.id, "name": self.name}
