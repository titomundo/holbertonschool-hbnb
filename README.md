# HolbertonSchool Basic Airbnb Project

#### This repository is meant to create a simple Python webapp using Flask

### Requirements
#### The app should have the following functions:
- User Management: Users can register, update their profiles, and be identified as either regular users or administrators.
- Place Management: Users can list properties (places) they own, specifying details such as name, description, price, and location (latitude and longitude). Each place can also have a list of amenities.
- Review Management: Users can leave reviews for places they have visited, including a rating and a comment.
- Amenity Management: The application will manage amenities that can be associated with places.

### Layers
#### The app is divided in three main layers
- Presentation Layer: This includes the services and API through which users interact with the system.
- Business Logic Layer: This contains the models and the core logic of the application.
- Persistence Layer: This is responsible for storing and retrieving data from the database.
