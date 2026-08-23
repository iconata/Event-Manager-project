# Project Setup Guide

This guide covers the initial setup required to get the Event Manager project running locally.

## Prerequisites

* [Docker Desktop](https://www.docker.com/products/docker-desktop/) installed and running.
* Python 3.13
* [uv](https://github.com/astral-sh/uv) (Python package manager)

* _If you're using MacOS:_
  * [colima](https://colima.run/#quick-start) if you're using an older OS version and Docker Desktop is not supported
  * `docker compose` installed through homebrew:
    * `brew install docker-compose`
### Optional
* [DBeaver](https://dbeaver.io/) (or another database client) installed.

## 1. Install dependencies
* In the terminal run:
  * `uv sync`

This will install all project dependencies and create a local virtual enviroment.

## 2. Create Local DB Configuration

Before running the project, you must create a configuration file.

1.  Find the file named `.env.example` in the root directory.
2.  Duplicate this file and rename the copy to `.env`.
3.  Fill in the values in the `.env` file (you can keep the defaults for local development).
4. .env is local, but still it should not be commited to GitHub.

## 3. Start the Database

The database runs in a Docker container.

```bash
# Start the database in detached (background) mode
docker compose up -d
```

## 4. Verify containers
* In the terminal execute:
  * `docker compose ps`
* PostgreSQL should be up and running.

## 5. Start up FastAPI
* In the terminal execute:
  * `uv run fastapi dev`
* Verify that the app is reachable by executing:
  * `curl -i 127.0.0.1/8080/`
    * The expected output should be:
      * `127.0.0.1:52365 - "GET / HTTP/1.1" 200

## 6. Verify that the tests are passing locally
* In the terminal execute:
  * `uv run python -m pytest`
    * All tests should pass


# Troubleshooting
#### Q: Docker compose is not starting or the command is not recognized.
    A: Install Docker desktop or Colima. Refer to section Prerequisites.


#### Q: The DB was build with the example env file, instead of a local copy of it.
    A: Execute docker compose down -v to shut down the docker daemon and refer to section 2.
    
***IMPORTANT NOTE***: _`-v` deletes the local PostgreSQL volume and all local database data_.
