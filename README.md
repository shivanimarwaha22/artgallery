# artgallery
The Goal of the Project "ART GALLERY & MARKETPLACE" :


We are building a backend for an Art Gallery and Marketplace application. The backend is the core “brain” of the application, responsible for handling data, managing user interactions, and ensuring secure access to different parts of the system.
In this project, users should be able to:
View artworks by different artists.
See detailed profiles of artists.
Add artworks to a cart and purchase them.
Manage their accounts if they’re a seller or buyer.
Order Status
The backend will store data (e.g., information about artworks), process user requests (e.g., adding an item to the cart), and secure the system (e.g., ensuring only authorized users can perform specific actions).
To achieve this, we use an API (Application Programming Interface) to connect the backend to the frontend.

Art Gallery and Marketplace API
This API (Application Programming Interface) is a behind-the-scenes system that powers an Art Gallery and Marketplace website. It manages users, artworks, artists, and orders, allowing the frontend (user interface) to connect to the backend (server) and perform actions like showing artworks, adding items to a cart, and making purchases.
 It has the “brain” of the website, where data lives and instructions are stored, so when users visit the site, they can view and interact with artworks effectively.
Project Setup
Step 1: Setting Up Django
Django is a powerful Python framework for building web applications, especially APIs. It provides tools for database management, authentication, and much more.
Why Django?
Efficiency: Django handles many complex tasks automatically, so we can focus on building the application’s functionality.
Security: Django has built-in security features to protect against common vulnerabilities.
Scalability: Django can manage large amounts of data and traffic, making it suitable for our Art Gallery API.

In Django, we first create a project using django-admin startproject artgallery to set up the main structure and configurations for the whole application. This project acts as the central "container" for the settings, database configurations, and URLs.
Then, we create an app within this project because Django organizes functionality into smaller, reusable modules called "apps." Each app can focus on a specific feature—like user management or the marketplace. This modular approach keeps the code organized and easy to maintain, allowing different apps to be reused in other projects if needed.
![image](https://github.com/user-attachments/assets/8a67a2ef-3c80-4b21-a592-34a32c142a92)


2. Defining the Data Structure with Models
What are Models?
Models are the blueprints for our data. Each model represents a “thing” we want to store, like an artist, an artwork, or a cart.
 In our Art Gallery app, we define models to represent users, artists, artworks, carts, and orders.
1. User Model
The User model represents anyone who interacts with the Art Gallery application. This includes buyers (who browse and purchase artworks) and sellers (who may upload or manage artworks).
Attributes (Data Stored):
USER_TYPES: Defines if the user is a "Buyer" or "Seller".
groups: Organizes users into groups for permissions (admin or manager, for example).
user_permissions: Lists special permissions the user may have.
Why It’s Needed: This model lets the app track who is using the system, their roles, and their permissions, ensuring each user has the correct access and capabilities.

2. Artist Model
The Artist model stores details about each artist who has artworks listed in the gallery. Each artist is linked to a user (as sellers must have a user account).
Attributes:
name: The artist’s name.
bio: A short biography of the artist.
user: Links the artist to a user account. This is a “one-to-one” relationship, meaning each artist has a unique user account.
Why It’s Needed: By separating artist details, we can manage and display artist information without mixing it up with general user data. This model provides a clear way to showcase the artist’s identity.

3. Artwork Model
The Artwork model represents each individual artwork in the gallery. Each artwork is linked to the artist who created it.
Attributes:
title: The artwork’s name.
description: A short description of the artwork.
price: The price of the artwork.
artist: Links the artwork to the artist who created it.
created_at: Automatically saves the date and time when the artwork was added to the gallery.
Why It’s Needed: This model enables the app to organize and display each piece of art individually, with relevant details and pricing information. It also ensures each artwork is linked to its artist, making it easy to track ownership and creator details.

4. Cart Model
The Cart model represents a shopping cart, where users can add artworks they intend to buy.
Attributes:
user: Links the cart to the user who owns it. This is a “many-to-one” relationship since each user can have multiple items in their cart.
artwork: The specific artwork that has been added to the cart.
quantity: The number of items for this artwork.
Why It’s Needed: This model keeps track of what each user has selected to purchase. By organizing items in a cart, users can add and review artworks before checking out.

5. Order Model
The Order model represents a completed purchase made by a user from the items in their cart.
Attributes:
user: Links the order to the user who placed it.
cart: Refers to the cart items included in the order.
ordered_at: Automatically saves the date and time when the order was placed.
status: The status of the order, like “Pending” or “Completed”.
Why It’s Needed: Orders allow the app to keep a record of completed purchases, helping both users and administrators track purchase history and status.

6. ApiRootView
The ApiRootView provides an overview of the main sections of the API, showing the user where they can access specific data and actions.
Purpose: This view gives a quick map of the API, listing each main endpoint (such as artists, artworks, carts, orders, and users). This makes it easier for developers or users interacting with the API to know where they can access data.




Explanation of Key Concepts
Models: Each model is a blueprint of a “thing” in our app (like User or Artwork), defining what details are stored for each one.
Relationships: Models are connected through relationships. For example, each artwork is linked to an artist, and each cart is linked to a user. This setup helps the app organize data clearly and efficiently.
One-to-One and Many-to-One:
One-to-One: Each artist has one unique user account.
Many-to-One: Each user can have multiple items in their cart, but each item belongs to only one user.
API Endpoints: These are specific URLs in the backend that provide access to data (e.g., /api/artists/ to access artist information).
Permissions: Controls who can access different parts of the app. For example, some users may only view artworks, while others can manage them.

3. Serializers: Converting Data for the API
What are Serializers?
Purpose
Serializers are used to convert complex data types (like Django models) into native Python data types that can then be easily rendered into JSON, XML, or other content types.
They also help in deserializing data, i.e., validating and converting incoming JSON data into Python objects that can be saved in the database.
Why We Use It
When building APIs, we often need to transform model instances into JSON data that can be sent over HTTP.
Serializers ensure data integrity by validating incoming data before saving it to the database.
They support advanced functionalities like nested relationships, field-level validation, and data transformations.

Serializers act as translators between our Django models and the JSON format used in APIs. They convert complex data (like an artwork object) into JSON so it can be sent over the internet to the frontend.
For example, an Artwork model instance might look like this in the database:

But in JSON format, it looks like this:
{
  "id": 1,
  "title": "Sunflower",
  "description": "Painting",
  "price": 100.0,
  "artist_id": 1
}



Why We Need Serializers
Data Transformation: Serializers transform Django models (which are complex Python objects) into simple, readable formats (like JSON) that can be sent over HTTP. This lets the frontend receive data in a standard way.
Data Validation: Serializers also validate incoming data before saving it to the database, ensuring that the data matches our expected format and requirements, which helps prevent errors and keeps the data consistent.
Serialization and Deserialization: They handle two-way data exchange: serialization (model to JSON) for sending data to the frontend, and deserialization (JSON to model) for receiving and saving data from the frontend.
Why JSON Format?
Universal Standard: JSON (JavaScript Object Notation) is a widely used data-interchange format that can be read by almost any programming language, making it ideal for frontend-backend communication.
Lightweight and Fast: JSON is compact and fast to process, reducing data load time and increasing responsiveness. Its text-based structure makes it easy to parse and understand, which is ideal for web applications.
Compatibility with JavaScript: JSON is directly compatible with JavaScript, the main language for frontend development. This makes JSON perfect for transferring data to frontend frameworks like React, as it’s natively understood by JavaScript.

4. Views: Defining Actions and Logic
Views are where we define the actions that can be taken in the API. Each view maps to a specific action, like viewing an artwork or adding it to a cart.
Purpose
Views handle the business logic of your application. They receive HTTP requests, interact with models and serializers, and return HTTP responses (usually JSON in the case of APIs).
In Django REST Framework, views can be function-based or class-based, with the latter being more common due to the flexibility and structure they provide.
Why We Use It
Views connect the backend logic to the frontend (or to an API client). They determine what data is fetched or saved and what response is returned.
Views also handle permissions, authentication, and other request-related processes.

In Django, we use viewsets, which are collections of actions related to a specific model. For example, an ArtworkViewSet might have actions to:
GET all artworks (view).
POST a new artwork (add).
PUT an existing artwork (edit).
DELETE an artwork (remove).
Why Do We Need Views?
Control Logic: Views control how data is accessed and manipulated, allowing us to enforce rules (like only allowing authenticated users to add items to the cart).
Respond to Requests: Views respond to requests from the frontend, returning data or performing actions.
5. Urls.py
Purpose
The urls.py file maps URLs (i.e., the endpoints) to specific views. It acts as a router to ensure that when a user visits a certain URL, the appropriate view function is executed.
Why We Use It
It allows us to define clean, organized URL structures for our APIs.
By separating URL patterns into different files (e.g., for each app), we keep the project modular and maintainable.
Example


serializers.py: Converts data between Django models and JSON (and vice versa).
views.py: Handles the business logic and request/response processing.
urls.py: Maps URLs to views, enabling users to access different endpoints.

6. Adding Authentication with JWT
What is Authentication?
Authentication verifies the identity of a user to ensure they are who they claim to be. In this project, we use JWT (JSON Web Tokens), a secure and efficient way to handle authentication.
Why Do We Need Authentication?
Security: Only authorized users should be able to perform certain actions (like adding items to a cart).
User Experience: Authentication provides a personalized experience, allowing users to access their data (like saved cart items).
How JWT Authentication Works
User Logs In: They send their username and password to the API.
API Issues a Token: If the credentials are valid, the API issues a JWT token.
User Accesses Secure Endpoints: The user includes the token with each request to prove their identity.
7. Documenting the API with Swagger
Swagger creates an interactive documentation page for our API, where each endpoint (e.g., /api/artists/) is listed with details on what it does.
Why Swagger is Important
Clarity: Shows all available actions, what data each requires, and the expected response.
Interactivity: Allows users to test the API directly from the browser.
Ease of Use: Helps developers understand and use the API without reading through complex code.

