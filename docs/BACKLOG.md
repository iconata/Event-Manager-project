# Product Backlog Direction

This document records the product boundaries behind the active GitHub backlog. GitHub issues and milestones remain the source for individual implementation stories and their current status.

## Product boundary

Event Manager is a provider-facing SaaS for children's-party animators, party agencies, and similar organizers. It is not a generic public event and RSVP application.

The initial workflow is:

1. a provider creates an account;
2. the provider creates or receives an initial Provider Workspace;
3. the provider defines a Service or Package;
4. the provider records a Customer;
5. the provider creates a Booking; and
6. the Booking stores essential party scheduling/details, a small status, and private operational notes.

All provider-owned data belongs to a Provider Workspace from the beginning.

## Current implementation order

After the remaining Milestone 1 documentation work:

### Milestone 2 — Persistence & Application Foundation

1. #52 Add application settings/configuration
2. #6 Install and Configure SQLAlchemy
3. #53 Add FastAPI database-session dependency

Milestone 2 is product-neutral and has no dependency on a provider-domain model.

### Milestone 3 — Accounts & Provider Workspace

1. #7 Define User model
2. #8 Add Alembic for Migrations
3. #68 Define Provider Workspace model
4. #23 Database Integration – FastAPI
5. #9 Provider Account Registration – API
6. #10 Login with JWT – FastAPI
7. #25 Protect API Endpoints with JWT
8. #81 Create provider workspace during onboarding

The domain model sequence then proceeds through Service or Package, Customer, and Booking/Party Details before CRUD workflows.

## Retired concepts

- RSVP stories are closed as not planned; RSVP is not another name for booking status.
- Generic Event stories have been deliberately replaced with Booking and Party terminology.
- Free/Pro plans are deferred; no payment infrastructure is planned.
- Multi-user agency membership and Owner/Admin/Member role systems are deferred until a single-provider workspace MVP is validated.
- Kubernetes is outside the product roadmap.

## Explicitly deferred product decisions

- Whether independent providers and agencies use exactly the same workspace model.
- Whether a provider may own or join multiple workspaces.
- Agency invitations, staff membership, and role permissions.
- The final Service versus Package terminology and the minimum pricing/duration fields.
- The exact Customer contact fields and privacy/retention policy.
- The smallest useful Booking status set.
- Whether completed/cancelled Bookings are archived, retained indefinitely, or later subject to deletion rules.
- Timezone, recurrence, travel-area, conflict detection, and calendar integration.
- Availability management after the core booking workflow.
- Which provider/profile fields may be explicitly published to Party Finder.
- Party Finder search, parent accounts, inquiries, reviews, ranking, and monetization.

These decisions should be made from provider workflow research rather than guessed during infrastructure or foundation work.
