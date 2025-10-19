# Project Setup Guide

This guide covers the initial setup required to get the Event Manager project running locally.

## Prerequisites

* [Docker Desktop](https://www.docker.com/products/docker-desktop/) installed and running.
* [DBeaver](https://dbeaver.io/) (or another database client) installed.
* Python 3.11+
* [uv](https://github.com/astral-sh/uv) (Python package manager)

## 1. Initial Configuration

Before running the project, you must create a configuration file.

1.  Find the file named `.env.example` in the root directory.
2.  Duplicate this file and rename the copy to `.env`.
3.  Fill in the values in the `.env` file (you can keep the defaults for local development).

***Note to user:*** *You should also create that `.env.example` file. Just copy your `.env` but remove the secret passwords, like this:*
`POSTGRES_PASSWORD=your_secret_password_here`

## 2. Start the Database

The database runs in a Docker container.

```bash
# Start the database in detached (background) mode
docker compose up -d