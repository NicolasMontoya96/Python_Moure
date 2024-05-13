from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Entidad user

class User(BaseModel):
    id: int
    name: str
    surname: str
    url: str
    age: int

users_list = [User(id=1,name="Nicolas",surname= "Montoya", url="https://moure.dev",age= 27),
            User(id=2, name="Brais", surname="Moure", url="https://nicolas.dev", age=20),
             User(id=3, name="Juan", surname="Perez", url="https://juan.dev", age=39)]


@app.get("/users")
async def users():
    return users_list

@app.get("/user/{id}")
async def user(id: int):
    users = filter(lambda user: user.id == id, users_list)
    try:
        return list(users)[0]
    except:
        return {"error": "No se ha encontrado el usuario"}

