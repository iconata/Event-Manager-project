Event Manager project with FastAPI, Flask, PostgreSQL, JWT, Kubernetes and Docker.

To install and use explore this project:
- Clone the repository: `git clone <project_url>`
- Navigate into the project directory: `cd <project_name>`
- Create a virtual environment: `uv venv`
- Activate the virtual environment:
	- **macOS/Linux (bash/zsh):** `source .venv/bin/activate`
	- **Windows (CMD):** `.venv\Scripts\activate.bat`
	- **Windows (PowerShell):** `.venv\Scripts\Activate.ps1`
- Install dependencies: `uv sync`
- Further steps to be added


## 📋 Project Progress Checklist

### 🟢 Milestone 1 – Project Setup & Foundations
- [x] Repository Initialization
- [x] Initialize Project with uv
- [x] Basic Dependency Installation
- [x] Directory Structure Setup
- [x] Bootstrap Flask Application
- [x] Bootstrap FastAPI Application
- [x] Basic CI Workflow Setup (GitHub Actions)
- [x] Developer Documentation – Setup Guide

### 🟡 Milestone 2 – Database Integration (PostgreSQL)
- [x] Setup PostgreSQL for Local Development
- [ ] Install and Configure SQLAlchemy
- [ ] Define Database Models
- [ ] Add Alembic for Migrations
- [ ] Database Integration – Flask
- [ ] Database Integration – FastAPI

### 🔵 Milestone 3 – User Accounts & Authentication
- [ ] User Registration – API
- [ ] User Registration – Web
- [ ] Login with JWT – FastAPI
- [ ] Session Login – Flask
- [ ] Protect API Endpoints with JWT
- [ ] Link Events and RSVPs to Users

### 🟣 Milestone 4 – Event Management
- [ ] Event Creation – Web
- [ ] Event Creation – API
- [ ] Event Listing – Web
- [ ] Event Listing – API
- [ ] RSVP to Event – API
- [ ] RSVP to Event – Web
- [ ] Event Detail View – Web

### 🟤 Milestone 5 – Deployment (Docker + Kubernetes)
- [ ] Create Dockerfile for Flask App (using uv)
- [ ] Create Dockerfile for FastAPI App (using uv)
- [ ] Setup PostgreSQL with Docker
- [ ] Create docker-compose.yml for Multi-Service Setup
- [ ] Add Healthcheck to Docker Compose
- [ ] Kubernetes Namespace and Config Setup
- [ ] Kubernetes Secrets for Credentials
- [ ] Kubernetes Deployment for Flask App
- [ ] Kubernetes Deployment for FastAPI App
- [ ] Kubernetes StatefulSet for PostgreSQL
- [ ] Ingress Controller for Flask & FastAPI
- [ ] CI/CD: Build and Push Docker Images
- [ ] CI/CD: Deploy to Kubernetes
