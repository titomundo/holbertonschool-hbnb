from app.models.base import BaseModel


class Amenity(BaseModel):
    def __init__(self, name: str):
        super().__init__()
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not name.strip():
            raise ValueError("Name cannot be empty")

        if len(name) > 50:
            raise ValueError("Name has a maximum length of 50 characters")

        self._name = name

    def as_dict(self):
        return {"id": self.id, "name": self.name}
