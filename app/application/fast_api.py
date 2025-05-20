from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.application.container import Container
from app.application.handler import Handlers
from typing import Final



def create_app() -> FastAPI:
    """
    Creates and configures the FastAPI application with its dependencies and routes.
    
    Returns:
        FastAPI: Configured FastAPI application instance
    """
    container: Final[Container] = Container()
    app: Final[FastAPI] = FastAPI(
        title="Poop Manager",
        description="API REST implemented with FastAPI and hexagonal architecture",
        version="1.0.0"
    )
    
     # CORS configuration
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["http://localhost", "http://localhost:3000", "http://localhost:8000", "http://127.0.0.1:3000", "http://127.0.0.1:8000", "http://localhost:4200", "https://vision.gaugelife.co"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    
    app.container = container
    
    for handler in Handlers.iterator():
        app.include_router(handler.router)
        
    return app