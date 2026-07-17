# Part 3: Enhanced Backend with Authentication and Database Integration
Now we start implementing Authentication using JWT tokens and persistent storage using databases like MySQL and SQLite.

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

### Auth Endpoints
| METHOD | ENDPOINT | RESULT |
|--------|----------|--------|
|POST|`/auth/login`|JWT Authentication token|

## Install and run
The app requires Python 3.10 or higher to run.
> You may have to use `python3` or `pip3` instead of `python` and `pip`.
```bash
python -m venv venv
source .venv/bin/activate
pip install -r requirements.txt
python run.py
```

### Initialize database
To start/restart the database remove the `instance/development.db` file and run:
```bash
sqlite3 instance/development.db < database/schema.sql
sqlite3 instance/development.db < database/seeder.sql
```

The application will be available at http://localhost:5000
