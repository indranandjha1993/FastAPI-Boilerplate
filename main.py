from fastapi import FastAPI

from app.api.routes import app as api_routes
from app.api.security import setup_security
from app.database.base import Base, engine

app = FastAPI()

app.include_router(api_routes)


@app.on_event("startup")
async def startup():
    await setup_security(app)
    Base.metadata.create_all(bind=engine)


@app.on_event("shutdown")
async def shutdown():
    await engine.disconnect()
