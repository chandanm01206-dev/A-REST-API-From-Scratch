# Production REST API

A production-ready, scalable REST API built with Python and FastAPI. This project is structured for a startup-grade backend system with features like JWT-based authentication, database integration (SQLAlchemy), and robust error handling.

## Tech Stack

* **Framework:** [FastAPI](https://fastapi.tiangolo.com/)
* **Database ORM:** [SQLAlchemy](https://www.sqlalchemy.org/)
* **Database Migrations:** [Alembic](https://alembic.sqlalchemy.org/)
* **Data Validation:** [Pydantic](https://docs.pydantic.dev/)
* **Authentication:** JWT (JSON Web Tokens) with `passlib` & `python-jose`
* **Server:** [Uvicorn](https://www.uvicorn.org/)

## Project Structure

```text
.
├── app/
│   ├── api/            # API routers (auth, users, etc.)
│   ├── core/           # Core configurations (security, dependencies)
│   ├── models/         # SQLAlchemy database models
│   ├── schemas/        # Pydantic schemas (data validation)
│   ├── config.py       # Environment configuration (pydantic-settings)
│   ├── database.py     # Database connection setup
│   └── main.py         # FastAPI application entry point
├── .env                # Environment variables (create this)
├── .gitignore
├── requirements.txt    # Project dependencies
└── test.db             # SQLite database (for local dev)
```

## Prerequisites

* Python 3.8+
* `pip` (Python package installer)

## Setup & Installation

1. **Clone the repository (if applicable) and navigate to the project root:**
   ```bash
   cd "REST API"
   ```

2. **Create and activate a virtual environment:**
   ```bash
   # Windows
   python -m venv venv
   venv\Scripts\activate
   
   # macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Environment Variables:**
   The project uses `pydantic-settings` to load configuration from a `.env` file. You should already have one, but ensure it contains the following keys:
   ```env
   PROJECT_NAME="Startup API"
   DATABASE_URL="sqlite:///./test.db"  # Or your PostgreSQL URL
   SECRET_KEY="your-super-secret-key"
   ALGORITHM="HS256"
   ACCESS_TOKEN_EXPIRE_MINUTES=30
   ```

## Running the Application

To start the development server, run:

```bash
uvicorn app.main:app --reload
```

The API will be available at: `http://localhost:8000`

## API Documentation

FastAPI automatically generates interactive API documentation. Once the server is running, you can access:

* **Swagger UI:** [http://localhost:8000/docs](http://localhost:8000/docs)
* **ReDoc:** [http://localhost:8000/redoc](http://localhost:8000/redoc)

## Core Endpoints

The API currently implements the following endpoint prefixes (check `/docs` for detailed schemas):

* **`GET /`**: Health check.
* **`/auth`**: Authentication endpoints (login/token generation).
* **`/users`**: User management endpoints (register, get current user, etc.).

## Database Migrations (Alembic)

*Note: For a fully production-ready database workflow, Alembic is included in `requirements.txt`. Currently, the app uses `Base.metadata.create_all()` in `main.py` for simplicity, but you can initialize Alembic with `alembic init alembic` to handle schema changes.*
