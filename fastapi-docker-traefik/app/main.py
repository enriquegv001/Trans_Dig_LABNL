from fastapi import FastAPI
from app.db import database, User
from pydantic import BaseModel

# Pydantic model for User input
class Item(BaseModel):
    email: str
    active: bool

app = FastAPI(title="FastAPI, Docker, and Traefik")

@app.get("/")
async def read_root():
    return await User.objects.all()

#@app.post("/items/")
#async def create_item(item: Item):
#    return item

@app.post("/users/")
async def create_user(user: Item):
    # Create a new user instance
    new_user = User(email=user.email, active=user.active)
    # Save the user to the database
    await new_user.save()
    return {"id": new_user.id, "email": new_user.email, "active": new_user.active}


        
