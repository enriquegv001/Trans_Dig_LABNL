<<<<<<< HEAD
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware 
import uvicorn 

# Create instance class
app = FastAPI() 

# Define Allowed Origins, from everywhere
origins = ['*']

# Cross-Origin Resource Sharing, handle request from different origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
) 

# Define Route function for application response after operation GET
@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}




# Run app if script run directly not run as module
if __name__ == "__main__":
    """
    Server as uvicorn
    Host in all network interfaces
    Listen to por 8000
    """
    uvicorn.run(app, host='0.0.0.0', port=8000)

    # Create table inside Postgres
    models.Base.metadata.create_all(bind=engine)
    app.include_router(posts.router)
=======
from fastapi import FastAPI, HTTPException, status, Query, Response
from fastapi.middleware.cors import CORSMiddleware 
import uvicorn 
from pydantic import BaseModel
from random import randrange, randint
import datetime

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
    email: str
    password: str
    nombre: str
    apellidos: str
    fechaNacimiento: str
    paisNacimiento: str
    telefono: str
    genero: str
    escolaridad: str
    codigoPostal: str
    estado: str
    ciudad: str
    colonia: str
    capacidadEspecial: str
    lenguaIndigena: str
    asociacion: str
    nombreAsociacion: str
    ocupacion: str
    deseasRecibirInformacion: str

class Registro(BaseModel):
    id: int
    nombre: str
    fechaAcceso: str
    actividad: str
    proyectoInscrito: str
    tuImagenPuedeSerCompartida: bool

class Login(BaseModel):
    email: str
    password: str

# User example
users = [
    {
        "email": "A01284184@tec.mx",
        "password": "1234",
        "nombre": "Daniel",
        "apellidos": "Loredo Melendez",
        "fechaNacimiento": "22/03/2002",
        "paisNacimiento": "Mexico",
        "telefono": "8112505850",
        "genero": "Masculino",
        "escolaridad": "Primaria",
        "codigoPostal": "67176",
        "estado": "Nuevo Leon",
        "ciudad": "Guadalupe",
        "colonia": "Bosques",
        "capacidadEspecial": "",
        "lenguaIndigena": "",
        "asociacion": "",
        "nombreAsociacion": "",
        "ocupacion": "Estudiante",
        "deseasRecibirInformacion": "",
    }
]

# Registro example 
registros = [
    # {
    #     "id": randint(1, 1000000),
    #     "user": "A01284184@tec.mx",
    #     "fechaAcceso": "22/13/2024",
    #     "actividad": "Uno libre",
    #     "proyectoInsccrito": "",
    #     "tuImagenPuedeSerCompartida": False
    # }
]

ultimoRegistro = {"id": 0}


# 1. GET all users (get)
@app.get("/users")
def get_all_users():
    # GET USERS in SQL TABLE
    return users

# 2. GET user by email (GET)
@app.get("/user/{email}")
def get_user_by_id(email: str):
    # GET USER BY EMAIL SQL
    selectedUser = {}
    for user in users:
        if user["email"] == email:
            selectedUser = user

    if not selectedUser:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User with correo electronico {email} not found")
    return {"user": selectedUser}

# 3. Crear usuario (POST)
@app.post('/signup')
def create_user(user: User):
    # POST USER connection SQL
    return {"user": user}

# 4. Login del usuario
@app.post('/login')
def login_user(login: Login):
    # CHECK IF THE email MATCH A PASSOWRD IN DATABSE
    user = get_user_by_id(login.email)
    return user

# 5. Validate a user from tap action in card
@app.post('/lecturaCredencial')
def lectura_credencial(email: str):
    # CHECK IF THE email EXIST IN SQL TABLE
    data = get_user_by_id(email)
    # ADD THE REGISTRO TO THE SQL DATABASE
    registroNuevo = buildRegistro(data["user"])

    return registroNuevo

# 6. Get all registros de acceso
@app.get('/registros')
def get_all_registros():
    return registros

# 7. Retornar registro
def buildRegistro(user: User):
    currentTime = datetime.datetime.now()

    nuevoRegistro = {
        "id": randint(1, 1000000),
        "nombre": user["nombre"] + " " + user["apellidos"],
        "fechaAcceso": currentTime,
        "actividad": "",
        "proyectoInscrito": "",
        "tuImagenPuedeSerCompartida": False
    }
    
    registros.append(nuevoRegistro)
    return nuevoRegistro

# 7. POST Registro
@app.post('/registro')
def crearRegistro(registro: Registro):
    # POST REGISTRO TO SQL DATABASE

    ultimoRegistro["id"] = registro.id
    return registro

@app.get('/revisarUltimoRegistro')
def revisar_ultimo_registro():
    # REGRESAR EL ULTIMO REGISTRO
    if(len(registros) > 0 and registros[-1]["id"] != ultimoRegistro["id"]):
        return registros[-1]
    else:
        return


if __name__ == "__main__":
    uvicorn.run(app, host='0.0.0.0', port=8000)
>>>>>>> c690af62fc886ebab014bdd840305541945e72e7
