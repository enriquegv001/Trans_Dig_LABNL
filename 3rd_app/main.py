#https://medium.com/datauniverse/building-crud-api-with-fastapi-a-step-by-step-guide-689b90f8234c

from fastapi import FastAPI, HTTPException, status, Query, Response
from pydantic import BaseModel
from typing import Optional
from random import randrange
from db import conn

app = FastAPI()

class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    ratings: Optional[int] = None


my_list = [
    {"title": "title of post 1", "content": "content of post 1", "id": 1},
    {"title": "title of post 2", "content": "content of post 2", "id": 2}
]

@app.get("/posts")
def get_all_posts():
    return {"data": my_list}

@app.post("/posts", status_code=status.HTTP_201_CREATED)
def create_post(post: Post):
    post_dict = post.dict()
    #post_dict["id"] = randrange(0, 1000000)
    #my_list.append(post_dict)

    cursor = conn.cursor()
    cursor.execute("INSERT INTO registros (nombre varchar(40), edad serial, genero VARCHAR(40), residencia VARCHAR(40), cp serial, estudios varchar(25),  ocupacion varchar(25), grupo_social varchar(25), actividad varchar(25), proyecto_labnl varchar(50), foto varchar(25), uso_datos varchar(25), correo varchar(25), recibir_info varchar(25)) VALUES (%(nombre)s, %(edad)s, %(genero)s, %(residencia)s, %(cp)s, %(estudios)s, %(ocupacion)s, %(grupos_social)s, %(actividad)s, %(proyecto_labnl)s, %(foto)s, %(uso_datos)s %(correo)s, %(recibir_info)s)", (**post_dict))
    #conn.commit()
    cursor.close()
    
    return {"data": post_dict}

    

"""
@app.get("/posts/latest")
def get_latest_post():
    post = my_list[-1]
    return {"post_detail": post}

@app.get("/posts/{id}")
def get_post_by_id(id: int):
    post = find_post(id)
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Post with ID {id} not found")
    return {"post_detail": post}

@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int):
    indx = find_index_post(id)
    if indx is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Post with ID {id} does not exist")
    my_list.pop(indx)
    return {"message": f"Post with ID {id} successfully deleted"}

def find_post(id):
    for p in my_list:
        if p["id"] == id:
            return p

def find_index_post(id):
    for i, p in enumerate(my_list):
        if p['id'] == id:
            return i
"""#https://medium.com/datauniverse/building-crud-api-with-fastapi-a-step-by-step-guide-689b90f8234c

from fastapi import FastAPI, HTTPException, status, Query, Response
from pydantic import BaseModel
from typing import Optional
from random import randrange

app = FastAPI()

class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    ratings: Optional[int] = None


my_list = [
    {"title": "title of post 1", "content": "content of post 1", "id": 1},
    {"title": "title of post 2", "content": "content of post 2", "id": 2}
]

@app.get("/posts")
def get_all_posts():
    return {"data": my_list}

@app.post("/posts", status_code=status.HTTP_201_CREATED)
def create_post(post: Post):
    post_dict = post.dict()
    post_dict["id"] = randrange(0, 1000000)
    my_list.append(post_dict)
    return {"data": post_dict}


"""
@app.get("/posts/latest")
def get_latest_post():
    post = my_list[-1]
    return {"post_detail": post}

@app.get("/posts/{id}")
def get_post_by_id(id: int):
    post = find_post(id)
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Post with ID {id} not found")
    return {"post_detail": post}

@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int):
    indx = find_index_post(id)
    if indx is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Post with ID {id} does not exist")
    my_list.pop(indx)
    return {"message": f"Post with ID {id} successfully deleted"}

def find_post(id):
    for p in my_list:
        if p["id"] == id:
            return p

def find_index_post(id):
    for i, p in enumerate(my_list):
        if p['id'] == id:
            return i
"""
