from fastapi import FastAPI, HTTPException, status, Query, Response
from fastapi.middleware.cors import CORSMiddleware 
import uvicorn 
from pydantic import BaseModel
from random import randrange

app = FastAPI() 

origins = [
    "*",
    "http://localhost",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
) 

@app.get("/")
async def root():
    return {"message": "Hello from Fastapi"} 

# Usuarios
class User(BaseModel):
    userName: str

class Registro(BaseModel):
    id: str
    registro: str


# User example
users = [{"id": "A01284184", "userName": "Daniel Loredo"}, {"id": "A01284184", "userName": "Mauricio Portilla"}]

# Registro example 
registros = [{"id": "A01284184", "registro": "Hola"}, {"id": "A01284184", "registro": "Hola"}]


# 1. GET all users (get)
@app.get("/users")
def get_all_users():
    return users

# 2. Crear usuario (POST)
@app.post('/user')
def create_user(user: User):
    newUser = user.__dict__
    newUser["id"] = randrange(0, 1000000)
    users.append(newUser)
    return {"new user": newUser}

# 3. GET user by id (GET)
@app.get("/user/{id}")
def get_user_by_id(id: int):
    # Buscar el usuiario por la id
    selectedUser = {}
    for user in users:
        if user["id"] == id:
            selectedUser = user

    if not selectedUser:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User with ID {id} not found")
    return {"user": selectedUser}


# 4. Borrar usuario (delete)
@app.delete('/user/{id}')
def delete_user(id: int):
    return {"usuario borrado": id}

# 5. Login del usuario

# 6. Get all registros de acceso
@app.get('/registros')
def get_all_registros():
    return registros

# 7. Registrar acceso (create)
@app.post('/registro')
def create_registro(registro: Registro):
    return registros


if __name__ == "__main__":
    uvicorn.run(app, host='0.0.0.0', port=8000)