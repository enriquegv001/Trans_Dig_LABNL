from fastapi import FastAPI
from app.db import database, User

app = FastAPI(title="FastAPI, Docker, and Traefik")

@app.get("/")
async def read_root():
    return await User.objects.all()

@app.on_event("startup") # Create database connection
async def startup():
    if not database.is_connected:
        await database.connect()
    # create a dummy entry
    await User.objects.get_or_create(email="test@test.com")

# Closes all connections to the databse
@app.on_event("shutdown")
async def shutdown():
    if database.is_connected:
        await database.disconnect()

        