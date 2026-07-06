# Part 2: Implementation of Business Logic and API Endpoints
In this step of the project we create the scaffold for our application and implement the models and business logic in order to create a basic RESTful API with CRUD operations. Only the `GET`, `POST` and `PUT` endpoints will be added for now. (The `DELETE` endpoints will be added later on the project). We will also create tests and validate our API.

## Structure
The project is built using the following structure.

```text
hbnb/
├── app/
│   ├── __init__.py
│   ├── api/
│   │   ├── __init__.py
│   │   ├── v1/
│   │       ├── __init__.py
│   │       ├── users.py
│   │       ├── places.py
│   │       ├── reviews.py
│   │       ├── amenities.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── user.py
│   │   ├── place.py
│   │   ├── review.py
│   │   ├── amenity.py
│   ├── services/
│   │   ├── __init__.py
│   │   ├── facade.py
│   ├── persistence/
│       ├── __init__.py
│       ├── repository.py
├── run.py
├── config.py
├── requirements.txt
├── README.md
```

- The `app/` folder includes the core logic of the application.
- The `api/` folder contains all the endpoints for requests.
- The `models/` folder defines the structures used to define objects for our aplication.
- The `services/` folder is a facade layer to interact between all application layers.
- The `persistence/` folder is used to interact with the database (in-memory storage for the time being).

## API Endpoints

> All API endpoints have the `/api/v1/` prefix. \
> Example: `/api/v1/users/<user_id>` will get the user for that specific ID

### User Endpoints
| METHOD | ENDPOINT | RESULT |
|--------|----------|--------|
|GET|`/users`|List of all users|
|GET|`/users/<user_id>`|Retrieve user by ID|
|POST|`/users`|Create a new user|
|PUT|`/users/<user_id>`|Update user by ID|

### Amenities Endpoints
| METHOD | ENDPOINT | RESULT |
|--------|----------|--------|
|GET|`/amenities`|List of all amenities|
|GET|`/amenities/<amenity_id>`|Retrieve amenity by ID|
|POST|`/amenities`|Create a new amenity|
|PUT|`/amenities/<amenity_id>`|Update amenity by ID|

### Place Endpoints
| METHOD | ENDPOINT | RESULT |
|--------|----------|--------|
|GET|`/places`|List of all places|
|GET|`/places/<place_id>`|Retrieve place by ID|
|POST|`/places`|Create a new place|
|PUT|`/place/<places_id>`|Update place by ID|

### Review Endpoints
| METHOD | ENDPOINT | RESULT |
|--------|----------|--------|
|GET|`/reviews`|List of all reviews|
|GET|`/reviews/<review_id>`|Retrieve review by ID|
|POST|`/reviews`|Create a new review|
|PUT|`/reviews/<review_id>`|Update review by ID|
|DELETE|`/reviews/<review_id>`|Delete review by ID|

## Install and run
> You may have to use `python` or `pip3` instead of `python` and `pip`.
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python run.py
```

The application will be available at http://localhost:5000
