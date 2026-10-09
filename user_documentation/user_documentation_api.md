# API — User documentation

## Solution overview

Ludotheque is a video game collection management application. It allows a user to browse a catalog, add games to their personal collection, rate and comment each title, and track their collection statistics.

It is designed for players and collectors who want to organize their game library in a simple and secure way. The application notably offers:

The Ludotheque API manages the different routes, such as Item, Auth, and Collection, through services that communicate with and update a database.
It provides several features, including:

- a game catalog with search and filtering by category;
- user registration and authentication;
- a private collection associated with each account;
- updating the status, rating, and comment for a game;
- global statistics on the collection.

## Quick start

Follow these steps to launch the project and access the API:

1. In the terminal, at the project root, run the following commands:

        py -m pip install -r api/requirements.txt
        cd api
        docker compose up -d
        cd ..
        py -m api.seed
        py -m uvicorn api.main:app --reload

2. Then open the API address in your browser:

        http://127.0.0.1:8000

3. Add `/docs` to the end of the URL to access the Swagger documentation:

        http://127.0.0.1:8000/docs

**Expected result:** you access the API Swagger documentation and can test the routes interactively.

## Feature guide

At first glance, you should see this:
![Swagger capture](../user_documentation/screen/apiSwagger.png)

### items

1. View the Items section available in Swagger with the following routes:

![Swagger capture](../user_documentation/screen/apiItemsSwagger.png)
---

2. The Collection routes allow:
    - browsing the list of games;
    - searching for a title, filtering by category, and viewing a game’s details.

3. These routes are accessible directly without authorization.

4. Each action includes parameters to fill in:
    - text search (`q`);
    - category (`categorie`);
    - page number (`page`);
    - number of items (`limit`);
    - search by identifier using (`item_id`).

**Expected result:** the user gets the list of available games or the details of a specific game without being authenticated.

### auth

1. View the Auth section available in Swagger with the following routes:

![Swagger capture](../user_documentation/screen/apiAuthSwagger.png)
---

2. The authentication routes allow:
    - creating an account with an email address and password;
    - logging in to receive a JWT token;
    - retrieving the current user.

3. The Authentication section is accessible via the “Authorize” button in Swagger, which also unlocks access to the collection.

4. For each action, parameters must be provided:
    - email and password for registration and login;
    - JWT token in the `Authorization` header for protected routes; `Authorization: Bearer <token>` pour les routes protégées ;
    - entry identifier (`entry_id`) to modify or delete a collection item.

**Résultat attendu :** l’utilisateur est authentifié et peut accéder aux routes protégées de sa collection personnelle.

### collection

1. View the Collection section available in Swagger with the following routes:

![Swagger capture](../user_documentation/screen/apiCollectionSwagger.png)
---

2. The Collection routes allow:
    - retrieving the user’s collection;
    - adding a game to the collection;
    - modifying a collection entry (status, rating, comment);
    - deleting a game from the collection;
    - retrieving collection statistics.

3. To access this section, the user must first authenticate. The routes are protected and require a valid token.

4. For each action, parameters must be provided (except when retrieving the collection and statistics):
    - to add a game, fill in `item_id`, `status`, `rating`, and `comment`;
    - to modify a game, provide the `entry_id` and the fields to update;
    - to delete a game, provide its `entry_id`.

**Expected result:** the user has a personal collection that can be consulted and modified, with statistics calculated automatically from their entries.

## Command list

| Command | Description |
|---|---|
| `py -m pip install -r api/requirements.txt` | Install Python dependencies. |
| `docker compose down -v` | Turn off the PostgreSQL database in Docker. |
| `docker compose up -d` | Start the PostgreSQL database in Docker. |
| `py -m api.seed` | Populate the database with the game data. |
| `py -m uvicorn api.main:app --reload` | Launch the API. |


## Prerequisites

- Python 3.12+;
- Node.js and npm;
- Docker Desktop or Docker Engine;
- an IDE such as VS Code;
- a browser.

## Access and configuration

1. Configuration: the `api/.env.example` file contains the variables to set. You must create a `.env` file with values adapted to the environment, notably:
   - `SECRET_KEY`;
   - `ALGORITHM`;
   - `ACCESS_TOKEN_EXPIRE_MINUTES`;
   - `DATABASE_URL`;
   - `CORS_ORIGINS`.
2. Help: if the project does not start, check that Docker is running, that the Python dependencies are installed, and that the `.env` file is correctly configured. The `README.md` files and the Swagger documentation help confirm that the routes are working properly.
