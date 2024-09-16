# Dockerized 3-Tier E-Commerce Application

## Overview
This project sets up a Dockerized 3-tier e-commerce application using two AWS EC2 instances. The frontend and backend are hosted on one instance, and the MySQL database is hosted on another instance.

## Architecture
- **Frontend & Backend**: Instance 1 (t2.micro Ubuntu)
- **Database (MySQL)**: Instance 2 (t2.micro Ubuntu)

## Prerequisites
- AWS EC2 setup with SSH access
- Docker and Docker Compose installed on both instances

## Setup

### 1. Launch EC2 Instances
- Launch two `t2.micro` instances with Ubuntu.
- Configure security groups:
  - Instance 1: Allow HTTP, HTTPS, SSH
  - Instance 2: Allow MySQL and SSH

### 2. Set Up Docker
Install Docker and Docker Compose on both instances.

### 3. Configure Frontend & Backend
- Create `Dockerfile` for both frontend and backend services.
- Set up `docker-compose.yml` to run both services and connect them to a shared Docker network.

### 4. Configure the Database
- Set up a MySQL container on the second instance.
- Configure the backend to connect to the MySQL container using the instance's private IP.

## Running the Application
On the frontend-backend instance, run:
```bash
docker-compose up --build -d
