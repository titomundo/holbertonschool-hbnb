from app.persistence.repository import InMemoryRepository
from app.models.user import User
from app.models.amenity import Amenity
from app.models.place import Place


class HBnBFacade:
    def __init__(self):
        self.user_repo = InMemoryRepository()
        self.place_repo = InMemoryRepository()
        self.review_repo = InMemoryRepository()
        self.amenity_repo = InMemoryRepository()

    #
    # User Methods
    #
    def create_user(self, user_data):
        user = User(**user_data)
        self.user_repo.add(user)
        return user

    def get_user(self, user_id):
        return self.user_repo.get(user_id)

    def get_all_users(self):
        return self.user_repo.get_all()

    def update_user(self, user_id, user_data):
        user = self.user_repo.update(user_id, user_data)

        if user:
            return user

    def get_user_by_email(self, email):
        return self.user_repo.get_by_attribute("email", email)

    #
    # Amenity Methods
    #
    def create_amenity(self, amenity_data):
        amenity = Amenity(**amenity_data)
        self.amenity_repo.add(amenity)
        return amenity

    def get_amenity(self, amenity_id):
        return self.amenity_repo.get(amenity_id)

    def get_all_amenities(self):
        return self.amenity_repo.get_all()

    def update_amenity(self, amenity_id, amenity_data):
        amenity = self.amenity_repo.update(amenity_id, amenity_data)

        if amenity:
            return amenity

    #
    # Place Methods
    #
    def create_place(self, place_data):
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

    def get_place(self, place_id):
        return self.place_repo.get(place_id)

    def get_all_places(self):
        return self.place_repo.get_all()

    def update_place(self, place_id, place_data):
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
