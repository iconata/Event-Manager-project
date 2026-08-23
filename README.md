# Event Manager

Event Manager is a learning project for building a small production-style SaaS for children's-party animators, party agencies, and similar party organizers.

The provider-facing application is the primary product. It will help providers organize their business, offerings, customers, and party bookings without introducing a large frontend or infrastructure ecosystem.

## Target users

- independent children's-party animators;
- small party agencies; and
- other providers who organize children's parties.

The first version assumes that each independent provider has one Provider Workspace representing their business. Multi-user agency membership and detailed staff roles may be considered later.

## Provider MVP

The initial product flow is deliberately small:

```text
Provider account
      |
      v
Provider Workspace
      |
      +----> Service / Package
      |
      +----> Customer
                  |
                  v
               Booking
                  |
                  v
       Party date, time, details,
       status, and operational notes
```

The MVP will eventually let a provider:

- register and authenticate;
- establish a business workspace;
- define services or party packages;
- record customers;
- create and manage bookings;
- store essential party details, booking status, and operational notes; and
- use a simple server-rendered browser interface.

Availability and calendar features may follow the core booking workflow. Payments, invoices, complex CRM automation, and multi-user agency administration are not part of the initial MVP.

## Later Party Finder direction

After the provider product is useful and has been tested through a first pilot, selected provider and service information may power a separate parent-facing Party Finder experience.

Party Finder is not part of the current MVP. Private workspace, customer, booking, party, and operational data must never become public by default.

## Technology stack

- Python
- FastAPI
- Pydantic
- SQLAlchemy
- PostgreSQL
- Alembic
- Jinja2
- pytest
- Docker and Docker Compose
- GitHub Actions
- JWT authentication

The project remains one FastAPI application backed by PostgreSQL. Kubernetes, microservices, Kafka, Redis, Celery, SPA frameworks, and payment infrastructure are not required.

## Current status

The FastAPI foundation is intentionally minimal. The application has a FastAPI-only entry point, a health endpoint, smoke tests, and aligned project metadata. Local setup documentation is the remaining open foundation task.

Persistence and product-domain functionality have not yet been implemented. The next implementation sequence begins with application settings, SQLAlchemy configuration, and the first provider-domain models.

See [the roadmap](docs/ROADMAP.md) for the milestone sequence and [the backlog](docs/BACKLOG.md) for current scope and deferred decisions.  
See [the setup guide](docs/SETUP.md) to run the project locally.
## Development philosophy

- Build one useful layer at a time.
- Keep the application understandable by one developer.
- Prefer working, testable outcomes over premature abstraction.
- Introduce infrastructure only when the product needs it.
- Treat provider data isolation and customer privacy as core requirements.
