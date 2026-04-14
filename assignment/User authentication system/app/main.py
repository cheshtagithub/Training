from pathlib import Path

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

from app.db.database import Base, engine
from app.models.user import User
from app.routes.auth import router as auth_router
from app.routes.dashboard import router as dashboard_router
from app.routes.profile import router as profile_router


BASE_DIR = Path(__file__).resolve().parent.parent
FRONTEND_DIR = BASE_DIR / "frontend"
PAGES_DIR = FRONTEND_DIR / "pages"

app = FastAPI(title="User Authentication System")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(auth_router)
app.include_router(dashboard_router)
app.include_router(profile_router)
app.mount("/frontend", StaticFiles(directory=FRONTEND_DIR), name="frontend")


@app.on_event("startup")
def on_startup() -> None:
    # Ensure model metadata is registered before creating tables.
    _ = User

    # Create database tables if they do not already exist.
    Base.metadata.create_all(bind=engine)


@app.get("/")
def read_root() -> dict[str, str]:
    return {"message": "FastAPI project is running"}


@app.get("/signup", include_in_schema=False)
def signup_page() -> FileResponse:
    return FileResponse(PAGES_DIR / "signup.html")


@app.get("/signup.html", include_in_schema=False)
def signup_page_html() -> FileResponse:
    return FileResponse(PAGES_DIR / "signup.html")


@app.get("/login", include_in_schema=False)
def login_page() -> FileResponse:
    return FileResponse(PAGES_DIR / "login.html")


@app.get("/login.html", include_in_schema=False)
def login_page_html() -> FileResponse:
    return FileResponse(PAGES_DIR / "login.html")


@app.get("/forgot-password", include_in_schema=False)
def forgot_password_page() -> FileResponse:
    return FileResponse(PAGES_DIR / "forgot-password.html")


@app.get("/forgot-password.html", include_in_schema=False)
def forgot_password_page_html() -> FileResponse:
    return FileResponse(PAGES_DIR / "forgot-password.html")


@app.get("/dashboard", include_in_schema=False)
def dashboard_page() -> FileResponse:
    return FileResponse(PAGES_DIR / "dashboard.html")


@app.get("/dashboard.html", include_in_schema=False)
def dashboard_page_html() -> FileResponse:
    return FileResponse(PAGES_DIR / "dashboard.html")


@app.get("/profile-page", include_in_schema=False)
def profile_page() -> FileResponse:
    return FileResponse(PAGES_DIR / "profile.html")


@app.get("/profile.html", include_in_schema=False)
def profile_page_html() -> FileResponse:
    return FileResponse(PAGES_DIR / "profile.html")


@app.get("/reset-password", include_in_schema=False)
def reset_password_page() -> FileResponse:
    return FileResponse(PAGES_DIR / "reset-password.html")


@app.get("/reset-password.html", include_in_schema=False)
def reset_password_page_html() -> FileResponse:
    return FileResponse(PAGES_DIR / "reset-password.html")


@app.get("/health")
def health_check() -> dict[str, str]:
    return {"status": "ok"}
