from app.api.v1.amenities import api as amenities_ns
from app.api.v1.auth import api as auth_ns
from app.api.v1.places import api as places_ns
from app.api.v1.reviews import api as review_ns
from app.api.v1.users import api as users_ns
from app.services import facade
from flask import Flask
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from flask_restx import Api


def create_app(config_class="config.DevelopmentConfig"):
    app = Flask(__name__)
    app.config.from_object(config_class)

    bcrypt = Bcrypt()
    bcrypt.init_app(app)

    jwt = JWTManager()
    jwt.init_app(app)

    api = Api(
        app,
        version="1.0",
        title="HBnB API",
        description="HBnB Application API",
        doc="/api/v1/",
    )

    # THESE USERS ARE TEMPORARY UNTIL WE GET PERSISTENT STORAGE 
    # AND WE CAN HAVE A DEFAULT ADMIN USER, THIS IS ONLY FOR TESTING
    facade.create_user(
        {
            "first_name": "admin",
            "last_name": "admin",
            "email": "admin@mail.com",
            "password": "password",
            "is_admin": True
        }
    )

    facade.create_user(
        {
            "first_name": "user",
            "last_name": "user",
            "email": "user@mail.com",
            "password": "password",
        }
    )

    # Placeholder for API namespaces (endpoints will be added later)
    api.add_namespace(users_ns, path="/api/v1/users")
    api.add_namespace(amenities_ns, path="/api/v1/amenities")
    api.add_namespace(places_ns, path="/api/v1/places")
    api.add_namespace(review_ns, path="/api/v1/reviews")
    api.add_namespace(auth_ns, path="/api/v1/auth")

    return app
