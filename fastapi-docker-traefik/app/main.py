from fastapi import FastAPI
from app.db import database, User

app = FastAPI(title="FastAPI, Docker, and Traefik")

@app.get("/")
async def read_root():
    return await User.objects.all()

@app.post("/users/")
async def create_user(user: UserBase):
    db_user = await User.objects.get_or_create(email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return db_user
    
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

        
