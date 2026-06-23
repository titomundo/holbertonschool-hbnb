from app.models.base import BaseModel
from app.models.user import User
from app.models.place import Place


class Review(BaseModel):
    def __init__(self, text: str, rating: int, place: Place, user: User):
        if 1 > rating > 5:
            raise ValueError("range must be between 1 and 5")

        super().__init__()
        self.text = text
        self.rating = rating
        self.place = place
        self.user = user
