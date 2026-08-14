# Event Manager Roadmap

This roadmap keeps Event Manager small while building it with patterns used in production Python backends. Each milestone should leave the project working and understandable before the next layer is added.

## Milestone 1 — FastAPI Foundation & Cleanup

**Goal:** Create a clean, consistent FastAPI-only foundation before adding application functionality.

Planned work:

- retire Flask from the target architecture;
- remove obsolete Flask application code when appropriate;
- standardize the Python version;
- clean project metadata;
- ensure FastAPI starts correctly;
- add `GET /health`;
- create basic smoke tests;
- align uv, CI, and documentation; and
- establish a simple, maintainable FastAPI project structure without overdesigning it.

## Milestone 2 — PostgreSQL & Persistence

**Goal:** Introduce proper database persistence.

Planned work:

- configure SQLAlchemy;
- configure the database engine and session factory;
- load database configuration from the environment;
- define the initial `User`, `Event`, and `RSVP` ORM models;
- configure Alembic and create initial migrations;
- implement a FastAPI `get_db()` dependency;
- verify PostgreSQL integration; and
- add database and integration tests.

Organizations are intentionally excluded from this milestone.

## Milestone 3 — Users & Authentication

**Goal:** Implement a production-style basic authentication flow.

Planned work:

- user registration and Pydantic schemas;
- password hashing;
- login and JWT access tokens;
- a current-user dependency;
- protected endpoints;
- authentication tests; and
- basic authorization.

Authentication should remain small and understandable. OAuth and social login are not planned yet.

## Milestone 4 — Core Event Management

**Goal:** Produce the first actually useful Event Manager.

Planned work:

- create events;
- list events and view event details;
- update and delete events;
- enforce owner permissions;
- create or update RSVPs;
- expose RSVP status and appropriate attendee counts/details; and
- test the core API workflows.

At the end of this milestone, the API should represent a usable MVP.

## Milestone 5 — Simple Web Experience

**Goal:** Provide a usable browser interface without introducing a separate frontend ecosystem.

Use FastAPI, Jinja2, HTML, minimal CSS, and minimal JavaScript only where useful.

Potential work:

- login and registration pages;
- event list and detail pages;
- event creation and edit forms; and
- RSVP controls.

React, Vue, and Angular are not part of this milestone.

## Milestone 6 — Production Readiness & First Deployment

**Goal:** Turn the local application into something that could realistically be hosted.

Planned work:

- create a FastAPI Dockerfile;
- provide a PostgreSQL and FastAPI Docker Compose setup;
- add container health checks;
- define environment configuration;
- run tests in CI and build a production image;
- add basic application logging;
- complete a first hosted deployment;
- consider basic database backups; and
- update setup and deployment documentation.

Kubernetes is not a requirement.

## Milestone 7 — SaaS Evolution

**Goal:** Only after the core application is useful, evolve it toward a basic SaaS architecture.

Planned concepts:

- an Organization, Workspace, or Tenant model;
- organization membership;
- Owner, Admin, and Member roles;
- organization-scoped events;
- tenant data isolation and authorization rules;
- tenant-isolation tests; and
- a simple Free/Pro subscription-plan model.

Initially, a subscription plan may be only a database field. Payment processing is not planned; Stripe or another provider should be considered only much later if the project reaches that point.
