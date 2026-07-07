# Part 1: Technical Documentation

## Introduction
In the first part of the project we will design the application architecture following a Facade Design Pattern. This means our app will be divided into three main layers:
- **Interace Layer**: The face of our app for the users to interact with.
- **Business Logic Layer**: The core logic and data models of our application.
- **Persistence Layer**: To manage connection with the database.

## Business Logic and Models
Within the Business Logic Layer we use the following models to describe the data used in our application:
- `User`: The main agent interacting with our application. Users can own places and create reviews. There should be a admin role for the hosts of the application.
- `Place`: The description of a physical place with their location (longitude and latitude), price and amenities. A place must have an owner (user) and can have multiple amenities and reviews.
- `Amenity`: The amenities a place can have. Such as Wi-Fi, pools, AC, etc. An amenity can belong to many places.
- `Review`: Users can write reviews and give ratings to places from 1 to 5. A review must be tied to a place and must belong to a user.

## The project is described using the following diagrams:

**1. High-Level Package Diagram:**
High-level package diagram that illustrates the three-layer architecture of the application and the communication between these layers via the facade pattern.

**2. Detailed Class Diagram for Business Logic Layer:** Class diagram for the Business Logic layer, focusing on the User, Place, Review, and Amenity entities, including their attributes, methods, and relationships.

**3. Sequence Diagrams for API Calls:** Sequence diagrams for examples of different API calls to show the interaction between the layers and the flow of information.

**4.Documentation Compilation:** Technical document describing the architecture and containing all diagramas with notes.
