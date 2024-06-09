from fastapi import FastAPI
from app.infrastructure.entry_point.routes import router

def create_app() -> FastAPI:
    app = FastAPI(title="ChaplinPoopManager", version="0.1")
    app.include_router(router)
    return app



app = create_app()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
    
