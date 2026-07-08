from app.models.base import BaseModel


class Review(BaseModel):
    def __init__(self, text: str, rating: int, place_id: str, user_id: str):

        super().__init__()
        self.text = text
        self.rating = rating
        self.place_id = place_id
        self.user_id = user_id

    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, text):
        if not text.strip():
            raise ValueError("Text cannot be empty")

        self._text = text

    @property
    def rating(self):
        return self._rating

    @rating.setter
    def rating(self, rating):
        if 1 > rating or rating > 5:
            raise ValueError("range must be between 1 and 5")

        self._rating = rating

    def as_dict(self):
        return {
            "id": self.id,
            "text": self.text,
            "place_id": self.place_id,
            "user_id": self.user_id,
        }
