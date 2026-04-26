from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database import engine, Base
from app.api.routes import auth, users
from app.config import settings

# Create database tables (In a real startup, we would use Alembic migrations instead)
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title=settings.PROJECT_NAME,
    description="A production-ready REST API",
    version="1.0.0"
)

# CORS Middleware to allow requests from the frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # In prod, restrict this to your frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include our routers
app.include_router(auth.router, prefix="/auth", tags=["Authentication"])
app.include_router(users.router, prefix="/users", tags=["Users"])

@app.get("/")
def health_check():
    return {"status": "ok", "message": "API is running"}
