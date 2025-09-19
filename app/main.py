from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager

from .routers import health, destinations, itineraries, marketplace, assistant, auth
from .database import connect_to_mongo, close_mongo_connection


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    await connect_to_mongo()
    yield
    # Shutdown
    await close_mongo_connection()


def create_app() -> FastAPI:
    app = FastAPI(
        title="Tourism Backend", 
        version="0.1.0",
        lifespan=lifespan
    )

    # Allow Expo/Web during development
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # Routers
    app.include_router(health.router)
    app.include_router(auth.router, prefix="/auth", tags=["authentication"])
    app.include_router(destinations.router, prefix="/destinations", tags=["destinations"])
    app.include_router(itineraries.router, prefix="/itineraries", tags=["itineraries"])
    app.include_router(marketplace.router, prefix="/marketplace", tags=["marketplace"])
    app.include_router(assistant.router, prefix="/assistant", tags=["assistant"])

    return app


app = create_app()


