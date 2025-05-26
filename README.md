# watchdxg-back

[![](https://img.shields.io/static/v1?label=Platform&message=Linux%20%7C%20macOS&color=deeppink)](#) [![](https://img.shields.io/static/v1?label=Python&message=v3.12&color=blue)](#) [![](https://img.shields.io/static/v1?label=Django&message=v5.2.1&color=coral)](#)

watchdxg-back is a self-hosted Django application designed to serve data populated from the watchdxg-core component. It is built to run on a single user’s private server and is structured with flexibility and simplicity in mind. This backend will be used by watchdxg-front, which is an Angular app designed to get informations on one's X account reputation management and statistics.

## 🔍 Overview

This project uses Django as the backend framework and includes:

- Django REST Framework (DRF) for API development.
- Simple JWT for token-based authentication.
- A PostgreSQL database that includes both Django-managed tables and custom external tables.
- A lightweight authentication model designed for personal, single-user use.

## 👤 Authentication Model

This application uses Django’s built-in user system for backend access, but only one Django user is ever created and used. The purpose of this user is not to represent the end user (i.e., the X account being analyzed), but rather to secure the API itself.

Front-end logins are "soft logins" — users enter an X handle, and the front end scopes data and actions accordingly. No actual authentication is done on the handle level. This handle is stored in the front-end state and/or used as a query parameter to fetch data for that identity.
Why This Design?

This architecture was chosen because:

- The system is single-user — there is no need for multi-user account management.
- The actual users (X accounts) are stored in a separate, existing table in the PostgreSQL database.
- Replacing Django's default user model would add unnecessary complexity.
- We want to benefit from Django and DRF’s tools (e.g., admin panel, permissions, token system) without disrupting the existing database structure.

## 🗄️ Database

The database contains:

- A standard Django schema, including auth_user.
- Custom tables, coming from watchdxg-core
- The Django models use managed = False when referencing external tables, so Django won’t try to alter them.

When deploying or running migrations, only Django-managed tables are affected.
API Security

All backend API routes are protected using JWT tokens. To interact with the backend:

- You must first obtain a token pair via the /api/token/ endpoint using the Django user credentials.
- Access tokens must be attached to future requests as Bearer tokens.

This ensures that the backend is never exposed publicly without authentication.
## 🤔 Frontend Behavior

The frontend provides a login screen that asks for an X handle. This is not a true login — it simply lets the frontend know what data to display. Only the user who owns the server has real access, via the Django user system.
Summary

- Use Django’s default user model, but only create and use one user.
- Authenticate backend access via JWT.
- Keep your X account data in its own table — no need to integrate deeply with Django’s auth system.
- The frontend simply selects a "view context" based on a handle.

This model is simple, secure, and ideal for the single-user scenario.


## 🚟 HTTP Requests

#### Get access and refresh tokens
```bash
curl -X POST http://localhost:8000/api/token/ \
    -H "Content-Type: application/json" \
    -d '{"username": "watchdxg", "password": "watchdxg"}'
```

#### Refresh a token
```bash
curl -X POST http://localhost:8000/api/token/refresh/ \
    -H "Content-Type: application/json" \
    -d '{"refresh": <Your refresh token>}'
```

#### Get X account by handle
```bash
curl -X GET "http://localhost:8000/api/accounts/<YourXUserHandle>/" \
  -H "Authorization: Bearer <Your access token>"
```

#### Get X users for a given X account

Just add the account id you got from the previous request
```bash
curl -X GET "http://localhost:8000/api/users/?account_id=<int>" \
  -H "Authorization: Bearer <Your access token>"
```