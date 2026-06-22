# Image Storage API

## Project Overview

This project is a REST API built using FastAPI that allows users to upload and retrieve images. The application stores image metadata in a SQLite database and saves image files on disk. The entire application is containerized using Docker and managed through Docker Compose.

### Features

* Upload images through a REST API
* Retrieve images using image ID
* Store image metadata in a SQLite database
* Containerized using Docker
* Docker Compose support
* Persistent image storage using Bind Mounts

---

## Project Structure

```text
image-storage-api/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── database.py
│   └── models.py
│
├── uploads/
│
├── images.db
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── README.md
└── .dockerignore
```

---

## API Endpoints

### Upload Image

**Endpoint**

```http
POST /upload
```

**Description**

Uploads an image to the server and stores its metadata in the database.

**Sample Response**

```json
{
  "id": 1,
  "filename": "sample.jpg"
}
```

---

### Retrieve Image

**Endpoint**

```http
GET /image/{image_id}
```

**Description**

Returns the image associated with the specified image ID.

**Example**

```http
GET /image/1
```

---

## Build Instructions

Build the Docker image using Docker Compose:

```bash
docker compose build
```

---

## Run Instructions

Start the application:

```bash
docker compose up
```

Run in detached mode:

```bash
docker compose up -d
```

Stop the application:

```bash
docker compose down
```

---

## Accessing the Application

### Swagger Documentation

Open the following URL in your browser:

```text
http://localhost:8000/docs
```

This provides an interactive interface for testing all API endpoints.

---

## Database

The application uses SQLite for storing image metadata.

Database file:

```text
images.db
```

Stored information:

* Image ID
* Filename
* File Path

---

## Docker Configuration

### Dockerfile

The application is packaged into a Docker image using a custom Dockerfile based on Python 3.11 Slim.

### Docker Compose

Docker Compose is used to:

* Build the image
* Create the container
* Expose application ports
* Configure persistent storage

---

## Volume / Bind Mount Configuration

The application uses a bind mount to persist uploaded images.

```yaml
volumes:
  - ./uploads:/app/uploads
```

### Explanation

| Host Machine | Container    |
| ------------ | ------------ |
| ./uploads    | /app/uploads |

Any image uploaded inside the container is stored in the host machine's `uploads` folder.

This ensures uploaded files remain available even if the container is stopped, removed, or recreated.

---

## Data Persistence Demonstration

1. Start the application using Docker Compose.
2. Upload an image using the `/upload` endpoint.
3. Verify that the image appears inside the local `uploads` directory.
4. Stop and remove the container:

```bash
docker compose down
```

5. Confirm that the image still exists in the local `uploads` folder.
6. Restart the application:

```bash
docker compose up -d
```

7. Retrieve the image using its image ID.

This demonstrates successful persistence using Docker Bind Mounts.

---

## Technologies Used

* Python 3.11
* FastAPI
* SQLAlchemy
* SQLite
* Docker
* Docker Compose

---

## Author

Ritik Mer
