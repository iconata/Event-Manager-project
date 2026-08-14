# Backlog Revision Proposal

This document proposes the issue and milestone migration to perform only after the roadmap PR is approved and merged. It preserves useful project history while replacing the former Flask/FastAPI split and premature Kubernetes work with a focused FastAPI learning path. No GitHub issues or milestones are changed by this PR.

## Keep and revise

These issues remain useful, but their descriptions and acceptance criteria should be rewritten for the FastAPI-only architecture and assigned to the new milestones.

- **#6 Install and Configure SQLAlchemy** — Configure SQLAlchemy only for the FastAPI application, including the engine and session factory. Target: Milestone 2.
- **#7 Define Database Models** — Define the initial `User`, `Event`, and `RSVP` ORM models without organizations or SaaS concepts. Target: Milestone 2.
- **#8 Add Alembic for Migrations** — Configure Alembic against the FastAPI application's SQLAlchemy metadata and create the initial migration. Target: Milestone 2.
- **#9 User Registration - API** — Implement FastAPI registration with validated schemas, password hashing, persistence, and tests. Target: Milestone 3.
- **#10 Login with JWT – FastAPI** — Implement a small FastAPI login flow that returns a JWT access token. Target: Milestone 3.
- **#13 Create Event – FastAPI** — Create authenticated event records through FastAPI and associate them with their owner. Target: Milestone 4.
- **#14 RSVP to Event – FastAPI** — Create or update a user's RSVP and expose its status through FastAPI. Target: Milestone 4.
- **#18 Create docker-compose.yml for Multi-Service Setup** — Orchestrate FastAPI and PostgreSQL, not Flask, FastAPI, and PostgreSQL. Consider whether Adminer remains a useful optional development profile. Target: Milestone 6.
- **#23 Database Integration – FastAPI** — Verify FastAPI-to-PostgreSQL integration through the database dependency and integration tests; distinguish it clearly from the lower-level SQLAlchemy setup stories. Target: Milestone 2.
- **#25 Protect API Endpoints with JWT** — Add the current-user dependency and apply it to protected FastAPI endpoints, with unauthorized-access tests. Target: Milestone 3.
- **#26 Link Events and RSVPs to Users** — Define and verify ownership and RSVP relationships for the core models. Target: Milestone 2, with authorization behavior completed in Milestone 4.
- **#28 Event Listing – API** — List events through FastAPI with clear response schemas and tests. Keep filtering or pagination modest unless needed. Target: Milestone 4.
- **#30 Add Healthcheck to Docker Compose** — Health-check both FastAPI and PostgreSQL and use dependency conditions where helpful. Target: Milestone 6.
- **#37 CI/CD: Build and Push Docker Images** — Build and, when appropriate, publish only the FastAPI application image; do not build Flask images or deploy to Kubernetes. Target: Milestone 6.

## Close as not planned

These Flask-specific issues should be retained as project history and closed as `not planned` after approval.

- **#11 Session Login - Flask** — Superseded by FastAPI JWT authentication and the later FastAPI/Jinja2 login experience.
- **#12 Create Event – Flask** — Superseded by the FastAPI event API and later FastAPI/Jinja2 event form.
- **#15 RSVP to Event – Flask** — Superseded by FastAPI RSVP endpoints and later Jinja2 RSVP controls.
- **#16 Create Dockerfile for Flask App** — No Flask application image belongs in the target architecture.
- **#22 Database Integration – Flask** — Persistence will be integrated only with FastAPI.
- **#24 User Registration – Web** — Close the Flask-oriented story; equivalent functionality may later be created with FastAPI and Jinja2.
- **#27 Event Listing – Web** — Close the Flask-oriented story; replace it with the planned FastAPI/Jinja2 event list page.
- **#29 Event Detail View – Web** — Close the Flask-oriented story; replace it with the planned FastAPI/Jinja2 event detail page.
- **#33 Kubernetes Deployment for Flask App** — Both Flask and required Kubernetes deployment are outside the roadmap.
- **#36 Ingress Controller for Flask & FastAPI** — The dual-framework ingress design is obsolete, and Kubernetes is not required.

## Defer / close as not planned for now

The following Kubernetes issues should be closed as `not planned` for the main product roadmap:

- **#31 Kubernetes Namespace and Config Setup**
- **#32 Kubernetes Secrets for Credentials**
- **#34 Kubernetes Deployment for FastAPI App**
- **#35 Kubernetes StatefulSet for PostgreSQL**
- **#38 CI/CD: Deploy to Kubernetes**

Kubernetes may become an optional, separate learning exercise in the future, but it is not required to build or deploy Event Manager and should not block the main learning path.

## Duplicate / superseded

- **#17 Setup PostgreSQL with Docker** — The repository already contains a PostgreSQL 16 Compose service, persistent volume configuration, environment placeholders, and local setup notes. Unless review identifies a specific unfinished outcome that is distinct from #18, close #17 as duplicate/superseded by the completed local-development work. Any remaining Compose integration should be captured by the revised #18 rather than duplicated.

## New stories to create

The stories below are intentionally small. Existing retained issues should be revised instead of recreated.

### Milestone 1 — FastAPI Foundation & Cleanup

#### Remove Flask from project architecture

Remove Flask code and dependencies once references have been checked, leaving FastAPI as the only application framework.

**Acceptance criteria:** Flask is absent from runtime dependencies and application entry points; FastAPI still starts; documentation contains no Flask target architecture.

#### Add FastAPI health endpoint

Add a lightweight endpoint for application and container health checks.

**Acceptance criteria:** `GET /health` returns HTTP 200 with a stable, documented response and does not require authentication.

#### Add FastAPI smoke tests

Add a minimal test suite proving the application can start and its basic endpoints respond.

**Acceptance criteria:** pytest covers the root and health endpoints; tests run locally without external services.

#### Align Python version and project metadata

Choose one supported Python version and replace placeholder package metadata.

**Acceptance criteria:** `pyproject.toml`, CI, and setup documentation agree on the Python version; project name and description are accurate.

#### Align CI with uv project environment

Make CI install and test the locked uv project environment.

**Acceptance criteria:** CI uses uv and the lockfile consistently, compiles or lints the application, and runs pytest without a placeholder test step.

#### Update local setup documentation

Document a tested FastAPI-first local workflow.

**Acceptance criteria:** setup covers prerequisites, environment creation, dependency installation, PostgreSQL startup, FastAPI startup, and tests; commands and Markdown render correctly.

### Milestone 2 — PostgreSQL & Persistence

#### Add application settings/configuration

Define typed application and database settings loaded from environment variables.

**Acceptance criteria:** development defaults are documented; secrets are not committed; invalid required configuration fails clearly.

#### Configure SQLAlchemy engine and session factory

Create the shared engine and session factory used by the FastAPI application.

**Acceptance criteria:** configuration supplies the database URL; sessions have explicit lifecycle behavior; a focused test verifies configuration.

#### Define User/Event/RSVP models

Model the initial application domain and its relationships.

**Acceptance criteria:** models include identifiers, necessary fields, timestamps where useful, event ownership, RSVP relationships, and appropriate constraints; no organization model is added.

#### Configure Alembic migrations

Connect Alembic to application metadata and establish the initial schema.

**Acceptance criteria:** migrations can upgrade a new database and downgrade cleanly; usage is documented.

#### Add FastAPI database-session dependency

Provide request-scoped database sessions through FastAPI dependency injection.

**Acceptance criteria:** `get_db()` yields a session, always closes it, and can be overridden in tests.

#### Add database integration tests

Verify persistence against PostgreSQL through the application database layer.

**Acceptance criteria:** tests cover connectivity and a basic create/read round trip; test setup is isolated and documented; CI execution is defined or explicitly staged.

### Milestone 4 — Core Event Management

#### Event Detail – API

Return one event and its appropriate RSVP summary.

**Acceptance criteria:** an existing event returns a validated response; a missing event returns 404; private data is not exposed.

#### Update Event – API

Allow an authenticated owner to edit an event.

**Acceptance criteria:** valid changes persist; non-owners are rejected; invalid input and missing events return appropriate errors; tests cover each case.

#### Delete Event – API

Allow an authenticated owner to delete an event.

**Acceptance criteria:** owners can delete; non-owners are rejected; dependent RSVP behavior is deliberate and tested; deleted or missing events return the documented result.

### Milestone 5 — Simple Web Experience

#### Configure Jinja2 templates in FastAPI

Add the shared template environment and a minimal base layout.

**Acceptance criteria:** FastAPI renders a tested template; static CSS is served; the setup remains small.

#### Create login page

Provide a server-rendered form for the existing authentication flow.

**Acceptance criteria:** users can submit credentials, see validation/authentication errors, and reach the authenticated experience after success.

#### Create registration page

Provide a server-rendered registration form.

**Acceptance criteria:** valid users can register; field and duplicate-account errors are shown safely; passwords are never rendered or logged.

#### Create event list page

Render the events available to the current user.

**Acceptance criteria:** events link to details; empty state and loading errors have useful output; the page is covered by a route test.

#### Create event detail page

Render event information and the appropriate attendee/RSVP summary.

**Acceptance criteria:** existing and missing events render correctly; owner-only controls appear only for the owner.

#### Create event form

Provide creation and editing forms backed by the event API/application logic.

**Acceptance criteria:** create and edit flows validate input, preserve useful values after errors, and enforce owner permissions.

#### Add RSVP controls

Allow authenticated users to set or change their RSVP from the event page.

**Acceptance criteria:** controls reflect current status; changes persist and update the page; unauthorized actions are rejected.

### Milestone 6 — Production Readiness & First Deployment

#### Create FastAPI Dockerfile

Build a focused production image for the FastAPI application.

**Acceptance criteria:** the image builds reproducibly, runs as a non-root user where practical, starts FastAPI, and excludes Flask.

#### Create FastAPI + PostgreSQL Docker Compose setup

Extend Compose to run the application and database together.

**Acceptance criteria:** one documented command starts both services; configuration comes from environment; persistent data and service dependencies are defined.

#### Add container health checks

Add meaningful health checks for the application and database containers.

**Acceptance criteria:** Compose reports both services healthy; FastAPI uses `/health`; startup tolerates normal database initialization time.

#### Add production configuration

Separate safe production settings from local defaults.

**Acceptance criteria:** required secrets and host/database settings are environment-driven; debug behavior is off by default in production; configuration is documented.

#### Add application logging

Provide useful, minimal runtime logs.

**Acceptance criteria:** startup, request, and unexpected error information is available without logging secrets; log level is configurable.

#### Deploy first hosted version

Deploy the FastAPI application and PostgreSQL using a straightforward hosting approach.

**Acceptance criteria:** the hosted health endpoint and core flow work over HTTPS; migrations and environment configuration are documented; basic backup considerations are recorded.

### Milestone 7 — SaaS Evolution

#### Define Organization model

Add the tenant entity after the MVP is stable.

**Acceptance criteria:** the model has a stable identifier, name, timestamps, and appropriate constraints; migration and model tests pass.

#### Define Organization Membership model

Represent user membership in organizations.

**Acceptance criteria:** memberships connect users and organizations uniquely and support a role; relationship constraints are tested.

#### Add organization roles

Introduce Owner, Admin, and Member permissions.

**Acceptance criteria:** role capabilities are documented in a small permission matrix and enforced by tested dependencies or application logic.

#### Scope events to organizations

Associate every tenant-owned event with one organization.

**Acceptance criteria:** schema and endpoints require organization context; migrations handle existing development data deliberately; cross-organization access is not allowed.

#### Enforce tenant isolation

Apply organization scope to reads and writes throughout the application.

**Acceptance criteria:** queries and mutations use the current organization; unauthorized tenant access returns a safe response; privileged roles do not bypass tenant boundaries.

#### Add tenant-isolation tests

Create focused regression coverage for cross-tenant boundaries.

**Acceptance criteria:** tests use at least two organizations and prove users cannot read, update, delete, or RSVP across tenant boundaries.

#### Add simple subscription-plan model

Represent Free and Pro plans without payment processing.

**Acceptance criteria:** an organization has a validated plan field with a safe default; plan checks can be tested; no billing provider or checkout flow is introduced.
