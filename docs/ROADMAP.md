# Event Manager Roadmap

Event Manager is being built as a small provider SaaS for children's-party animators, party agencies, and similar organizers. The roadmap keeps the architecture simple while introducing the Provider Workspace boundary before provider-owned data.

## Milestone 1 — FastAPI Foundation & Developer Workflow

**Goal:** Complete the FastAPI-only foundation and establish a consistent local and CI developer workflow before persistence and product work begins.

Completed foundation work includes retiring Flask, adding `GET /health`, adding smoke tests, aligning Python/project metadata, and aligning CI with the uv environment. The milestone remains open until local setup documentation is current and reproducible.

## Milestone 2 — Persistence & Application Foundation

**Goal:** Introduce product-neutral configuration and PostgreSQL persistence.

Planned outcomes:

- typed application and database settings;
- SQLAlchemy engine and session factory;
- request-scoped FastAPI database sessions;
- Alembic configuration and migrations; and
- PostgreSQL integration testing.

The expected implementation order begins with #52, followed by #6. Domain models follow only after this foundation exists.

## Milestone 3 — Accounts & Provider Workspace

**Goal:** Add authenticated provider accounts and establish Provider Workspace as the tenant boundary.

Planned outcomes:

- User persistence;
- provider account registration;
- JWT login and current-user authentication;
- the initial Provider Workspace model; and
- creation of a provider's first workspace during onboarding.

The first MVP supports a simple independent-provider model. Multi-user agency membership, invitations, and richer roles are deferred.

## Milestone 4 — Provider Operations MVP

**Goal:** Build the operational core a children's-party provider can use.

Planned outcomes:

- workspace-owned Service or Package records;
- workspace-owned Customer records;
- Booking and Party Details records;
- booking creation, listing, detail, updates, and a small cancellation/archive lifecycle;
- private operational notes and booking status;
- workspace-scoped provider data; and
- tenant-isolation tests.

Booking is the central operational concept. RSVP and generic public Event behavior are not part of the provider MVP.

Availability and calendar capabilities may follow once the core booking workflow is useful.

## Milestone 5 — Provider Web Experience

**Goal:** Provide a small server-rendered interface for provider workflows.

Use FastAPI, Jinja2, HTML, minimal CSS, and minimal JavaScript where useful.

Planned outcomes:

- login and provider registration pages;
- provider workspace setup;
- Service or Package management;
- Customer management; and
- Booking list, detail, create, and edit experiences.

A separate SPA frontend is not planned.

## Milestone 6 — Production Readiness & First Pilot

**Goal:** Host the provider application for a small first pilot using a straightforward production-oriented setup.

Planned outcomes:

- a focused FastAPI container image;
- FastAPI and PostgreSQL Docker Compose configuration;
- container health checks;
- production environment configuration;
- application logging;
- CI image builds; and
- a documented first hosted deployment with basic backup considerations.

Kubernetes and distributed infrastructure are not required.

## Milestone 7 — Party Finder Foundation

**Goal:** After the provider MVP is proven, define a privacy-conscious read-only foundation for selected public provider data.

Planned outcomes:

- explicit provider publication settings, disabled by default;
- allow-listed public provider and service/package projections;
- a read-only public API boundary; and
- privacy tests that prevent customer, booking, party, notes, credential, and internal workspace data from leaking.

This milestone does not include a Party Finder UI, parent accounts, reviews, rankings, inquiries, marketplace payments, or a separate service.
