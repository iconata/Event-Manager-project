# Project Setup Guide

This guide covers the initial setup required to get the Event Manager project running locally.

## Prerequisites

* [Docker-compatible runtime](https://www.docker.com/products/) installed and running.
* Python 3.13
* [uv](https://github.com/astral-sh/uv) (Python package manager)
* Docker Compose

* _For example:_
  * [Colima](https://colima.run/#quick-start) 
  * [Docker Desktop](https://www.docker.com/products/docker-desktop/)

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

If you've intalled Colima, it's mandatory to execute:
`colima start`
otherwise the daemon will not be started.

```bash
# Start the database in detached (background) mode
docker compose up -d
```

```bash
# Stop the local stack without deleting the volumes
docker compose down
```

## 4. Verify containers
* In the terminal execute:
  * `docker compose ps`
* PostgreSQL should be up and running.

## 5. Start up FastAPI
* In the terminal execute:
  * `uv run fastapi dev`
* Verify that the app is reachable by executing:
  * `curl -i http://127.0.0.1:8000/health`
    * The expected output should be:
      * `HTTP/1.1 200 OK`
      * `content-type: application/json`

## 6. Verify that the tests are passing locally
* In the terminal execute:
  * `uv run python -m pytest`
    * All tests should pass


# Troubleshooting
**Q:** Docker compose is not starting or the command is not recognized.  
**A:** Install Docker desktop or Colima. Refer to section Prerequisites.


**Q:** The DB was build with the example env file, instead of a local copy of it.  
**A:** Execute docker compose down -v to remove the compose containers/network and deletes the named volumes.
    
***IMPORTANT NOTE***: _`-v` deletes the local PostgreSQL volume and all local database data_.
