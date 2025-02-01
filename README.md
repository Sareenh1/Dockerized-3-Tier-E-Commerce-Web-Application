# Dockerized 3-Tier E-Commerce Application: A Step-by-Step Guide

In today's fast-paced development world, containerization has become a game-changer for building, deploying, and scaling applications. Docker, one of the most popular containerization tools, allows developers to package applications and their dependencies into lightweight, portable containers. In this blog post, I’ll walk you through how I dockerized a 3-tier e-commerce application using React for the frontend, Node.js/Express for the backend, and MySQL for the database.

---

## What is a 3-Tier Architecture?

A 3-tier architecture separates an application into three logical layers:

1. **Frontend (Presentation Layer)**: Handles the user interface and user interactions. In this project, I used **React**.
2. **Backend (Application Layer)**: Manages business logic, processes requests, and interacts with the database. I used **Node.js** with **Express** for this layer.
3. **Database (Data Layer)**: Stores and retrieves data. I used **MySQL** as the database.

By containerizing each tier, we can ensure better portability, scalability, and consistency across different environments.

---

## Why Dockerize?

Dockerizing the application offers several benefits:

- **Portability**: Run the application consistently across different environments (development, testing, production).
- **Isolation**: Each service runs in its own container, avoiding dependency conflicts.
- **Scalability**: Easily scale individual services as needed.
- **Simplified Development**: Developers can quickly set up the entire stack with a single command.

---

## Steps to Dockerize the 3-Tier E-Commerce App

### 1. Create Separate Dockerfiles for Each Service

Each tier of the application has its own `Dockerfile` to define how the container should be built.

#### Frontend (React) Dockerfile
```dockerfile
# Use the official Node.js image as the base
FROM node:16

# Set the working directory
WORKDIR /app

# Copy package.json and install dependencies
COPY package.json .
RUN npm install

# Copy the rest of the application code
COPY . .

# Build the React app
RUN npm run build

# Expose port 3000 for the frontend
EXPOSE 3000

# Start the application
CMD ["npm", "start"]
```

#### Backend (Node.js/Express) Dockerfile
```dockerfile
# Use the official Node.js image as the base
FROM node:16

# Set the working directory
WORKDIR /app

# Copy package.json and install dependencies
COPY package.json .
RUN npm install

# Copy the rest of the application code
COPY . .

# Expose port 5000 for the backend
EXPOSE 5000

# Start the application
CMD ["node", "server.js"]
```

#### MySQL Dockerfile
For MySQL, we can use the official MySQL image directly in the `docker-compose.yml` file, so no separate `Dockerfile` is needed.

---

### 2. Define Multi-Container Services with Docker Compose

The `docker-compose.yml` file defines how the containers interact with each other.

```yaml
version: '3.8'

services:
  frontend:
    build: ./frontend
    ports:
      - "3000:3000"
    depends_on:
      - backend
    environment:
      - REACT_APP_API_URL=http://localhost:5000

  backend:
    build: ./backend
    ports:
      - "5000:5000"
    depends_on:
      - db
    environment:
      - DB_HOST=db
      - DB_USER=root
      - DB_PASSWORD=password
      - DB_NAME=ecommerce

  db:
    image: mysql:5.7
    ports:
      - "3306:3306"
    environment:
      - MYSQL_ROOT_PASSWORD=password
      - MYSQL_DATABASE=ecommerce
    volumes:
      - mysql-data:/var/lib/mysql

volumes:
  mysql-data:
```

---

### 3. Build and Launch the Containers

To build and start the containers, run the following command:

```bash
docker-compose up --build
```

This command:
- Builds the images for the frontend and backend.
- Pulls the MySQL image.
- Starts all the containers and ensures they can communicate with each other.

---

### 4. Test the Application Locally

Once the containers are up and running, you can access the application locally:

- **Frontend**: Open your browser and navigate to `http://localhost:3000`.
- **Backend**: The backend API is available at `http://localhost:5000`.

---

### 5. Manage the Lifecycle of the Containers

To stop and remove the containers, use the following command:

```bash
docker-compose down
```

This command stops and removes all the containers, networks, and volumes defined in the `docker-compose.yml` file.

---

## Key Benefits Achieved

By dockerizing this 3-tier e-commerce application, I was able to:

1. **Improve Portability**: The entire application can be run on any machine with Docker installed.
2. **Ensure Consistency**: The same environment is replicated across development, testing, and production.
3. **Simplify Scaling**: Individual services can be scaled independently as needed.
4. **Streamline Development**: Setting up the entire stack is as simple as running `docker-compose up`.

---

## Conclusion

Dockerizing a 3-tier application might seem daunting at first, but it’s a powerful way to modernize your development workflow. By following the steps outlined in this post, you can containerize your own applications and reap the benefits of portability, scalability, and consistency.
