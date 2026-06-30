from fastapi import FastAPI

from app.database import Base, engine

# Import all models
from app.models import user
from app.models import book
from app.models import member
from app.models import issue

# Import routers
from app.routes.auth_routes import router as auth_router
from app.routes.book_routes import router as book_router
from app.routes.member_routes import router as member_router
from app.routes.issue_routes import router as issue_router


# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Library Management System",
    version="1.0.0",
    description="Library Management APIs using FastAPI"
)


@app.get("/")
def home():
    return {
        "message": "Library Management System API is Running"
    }


app.include_router(auth_router)
app.include_router(book_router)
app.include_router(member_router)
app.include_router(issue_router)