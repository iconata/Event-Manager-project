# Event Manager

> **Build Event Manager as a small production-style FastAPI application that can gradually evolve into a multi-tenant SaaS.**

Event Manager is a learning project focused on modern Python backend development. The immediate aim is to build a small, useful application with production-oriented patterns while keeping the code understandable. If the core application proves useful, it may eventually evolve into a small hosted SaaS product; it is not a commercial SaaS today.

## What the application will do

The initial application will eventually let users:

- register and log in;
- create events;
- list and view events;
- update or delete events they own;
- RSVP to events; and
- view attendees and RSVP status.

After the MVP is useful, later SaaS evolution may add organizations or workspaces, organization membership, Owner/Admin/Member roles, tenant-isolated data, simple Free/Pro plan concepts, and hosted deployment. These are future capabilities, not part of the MVP.

## Technology stack

- Python
- FastAPI
- Pydantic
- SQLAlchemy
- PostgreSQL
- Alembic
- Jinja2 for a simple server-rendered UI
- Docker and Docker Compose
- pytest
- GitHub Actions
- JWT authentication

Kubernetes is not required for this project. It may be explored separately as an optional learning exercise in the future.

## Architecture direction

```text
Browser / API client
        |
        v
     FastAPI
     /     \
JSON API   Jinja2 UI
     \     /
   Application logic
        |
        v
    SQLAlchemy
        |
        v
    PostgreSQL
```

The architecture will stay deliberately simple: one FastAPI application, one database, and clear application boundaries introduced only when they are useful.

## Learning goals

This project is intended to teach practical REST API design, request and response validation with Pydantic, dependency injection, database sessions, ORM concepts, schema migrations, authentication and authorization, testing, containerization, CI, and a production-oriented application structure. Multi-tenancy will be studied later, after the core application works.

## Development philosophy

- Build one useful layer at a time.
- Prefer a working, simple solution over premature abstraction.
- Introduce infrastructure only when the application needs it.
- Keep the project understandable by one developer.
- Prioritize learning and comprehension over maximum feature count.

See [the roadmap](docs/ROADMAP.md) for the planned development sequence and [the backlog revision proposal](docs/BACKLOG_REVISION.md) for the issue and milestone changes proposed after this documentation is approved.
