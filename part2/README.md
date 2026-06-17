# System design and structure

## HBNB Project

This python application is using a Facade Design Pattern to implement Logic, Business and Presentation layers.

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

- The app/ folder includes the core logic of the application.
- The api/ folder contains all the endpoints for requests.
- The models/ folder defines the structures used to define objects for our aplication.
- The services/ folder is a facade layer to interact between all application layers.
- The persistence/ folder is used to interact with the database (in-memory storage for the time being).

## Install and run

```bash
pip install -r requirements.txt
python run.py
```
