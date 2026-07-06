from app.persistence.repository import InMemoryRepository
from app.models.user import User
from app.models.amenity import Amenity
from app.models.place import Place
from app.models.review import Review


class HBnBFacade:
    def __init__(self):
        self.user_repo = InMemoryRepository()
        self.place_repo = InMemoryRepository()
        self.review_repo = InMemoryRepository()
        self.amenity_repo = InMemoryRepository()

    #
    # User Methods
    #
    def create_user(self, user_data) -> User:
        user = User(**user_data)
        self.user_repo.add(user)
        return user

    def get_user(self, user_id) -> User | None:
        return self.user_repo.get(user_id)

    def get_all_users(self) -> list[User]:
        return self.user_repo.get_all()

    def update_user(self, user_id, user_data) -> User | None:
        return self.user_repo.update(user_id, user_data)

    def get_user_by_email(self, email) -> User | None:
        return self.user_repo.get_by_attribute("email", email)

    #
    # Amenity Methods
    #
    def create_amenity(self, amenity_data) -> Amenity:
        amenity = Amenity(**amenity_data)
        self.amenity_repo.add(amenity)
        return amenity

    def get_amenity(self, amenity_id) -> Amenity | None:
        return self.amenity_repo.get(amenity_id)

    def get_all_amenities(self) -> list[Amenity]:
        return self.amenity_repo.get_all()

    def update_amenity(self, amenity_id, amenity_data) -> Amenity | None:
        return self.amenity_repo.update(amenity_id, amenity_data)

    #
    # Place Methods
    #
    def create_place(self, place_data) -> Place:
        price = place_data.get("price")
        latitude = place_data.get("latitude")
        longitude = place_data.get("longitude")

        if price < 0.0:
            raise ValueError("Price should be a non-negative Float")
        if -90.0 > latitude or latitude > 90.0:
            raise ValueError("Latitude range must be between -90.0 and 90.0")
        if -180.0 > longitude or longitude > 180.0:
            raise ValueError("Longitude range must be between -180.0 and 180.0")

        place = Place(**place_data)
        self.place_repo.add(place)
        return place

    def get_place(self, place_id) -> Place | None:
        return self.place_repo.get(place_id)

    def get_all_places(self) -> list[Place]:
        return self.place_repo.get_all()

    def get_reviews_by_place(self, place_id) -> list[Review]:
        reviews = []
        for review in self.review_repo._storage.values():

            if review.place_id == place_id:
                reviews.append(review)

        return reviews

    def update_place(self, place_id, place_data) -> Place | None:
        price = place_data.get("price")
        latitude = place_data.get("latitude")
        longitude = place_data.get("longitude")

        if price < 0.0:
            raise ValueError("Price should be a non-negative Float")
        if -90.0 > latitude or latitude > 90.0:
            raise ValueError("Latitude range must be between -90.0 and 90.0")
        if -180.0 > longitude or longitude > 180.0:
            raise ValueError("Longitude range must be between -180.0 and 180.0")

        place = self.place_repo.update(place_id, place_data)

        if place:
            return place

    #
    # Review Methods
    #
    def create_review(self, review_data) -> Review | None:
        review = Review(**review_data)

        if review:
            self.review_repo.add(review)

        return review

    def get_review(self, review_id) -> Review | None:
        return self.review_repo.get(review_id)

    def get_all_reviews(self) -> list[Review]:
        return self.review_repo.get_all()

    def update_review(self, review_id, review_data) -> Review | None:
        rating = review_data.get("rating")
        if 1 > rating or rating > 5:
            raise ValueError("range must be between 1 and 5")

        place = self.review_repo.update(review_id, review_data)
        return place

    def delete_review(self, review_id):
        # TODO: ensure there is no leftover data with relationships to places
        self.review_repo.delete(review_id)
