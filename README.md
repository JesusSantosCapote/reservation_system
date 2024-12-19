# Requirements

- Docker installed
- A web browser installed: Chrome, Edge, Safari, etc.

# Set Up

1. If you have Docker Desktop, open it.
2. Open a terminal in the directory where the `docker-compose.yaml` file is located.
3. Execute the command: `docker compose up`.
4. Wait for the images to be created and the containers to be mounted.
5. Open your web browser and go to: `http://0.0.0.0:8000`.
6. Navigate through the routes displayed on the screen. Done!

# Project Description

An API created with Django Rest Framework with endpoints to manage clients and reservations. Fully Dockerized, it includes services (containers) for the API, a MySQL database, Celery for sending asynchronous emails to clients when reservations are created, and a RabbitMQ service as the broker for Celery.
