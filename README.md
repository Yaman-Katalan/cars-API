# Cars Store

**Author:** Mohamed Yaman Katalan

**Date:** August 8, 2024

## Description

The "Cars Store" project is a Django-based web application designed to manage car listings and their associated details. This application provides a RESTful API for CRUD operations on car records, enabling users to create, read, update, and delete car entries. The application uses PostgreSQL as its database backend and incorporates Docker for containerization to ensure a consistent development and deployment environment.

### Features

- **CRUD Operations:** Users can create, read, update, and delete car listings.
- **Authentication:** Users must be authenticated to perform create, update, or delete operations.
- **Custom Permissions:** Implemented custom permissions to ensure users can only modify their own car listings.
- **Dockerized:** The application is containerized using Docker and Docker Compose for easy deployment and management.

### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/your-username/cars_store.git
   cd cars_store
   ```

2. **Build and start the Docker containers:**

   ```bash
   docker-compose build
   docker-compose up -d
   ```

3. **Run migrations:**

   ```bash
   docker-compose run web python manage.py migrate
   ```

4. **Access the application:**

   Open your browser and go to `http://localhost:8000` to interact with the application.

### Dependencies

- Django 5.0.7
- Django REST Framework 3.15.2
- psycopg2-binary 2.9.9
- PostgreSQL

### Usage

- **List Cars:** `GET /api/cars/`
- **Create Car:** `POST /api/cars/`
- **Retrieve Car Details:** `GET /api/cars/<id>/`
- **Update Car:** `PUT /api/cars/<id>/`
- **Delete Car:** `DELETE /api/cars/<id>/`
