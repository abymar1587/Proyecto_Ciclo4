from fastapi import FastAPI
from pydantic import BaseModel #para declarar un request body se debe importar BaeModel de pydantic
from typing import Union


class Item(BaseModel): ##se mandan datos de un cliente a la API, se utilizara la operacion post(ingresar nueva informacion)
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None

#instancia
app = FastAPI()

#path-operations-functions
#Metodos get

#Ruta root-ruta principal
@app.get("/") #path:"/", operation:get
async def root(): #function: root() [corresponde a la funcion que se encuentra debajo del decorador]
    return {"message": "Hello World"}

#fixed path(path fijo, en la misma ruta de un pathh parameters "users"), se debe declarar antes de path parameters, de este modo el codigo no asumira que "me" corresponde a un path parameter
@app.get("/users/me")
async def read_user_me():
    return {"user_id": "Aury Margarita Nuñez Campo"}

@app.get("/users/{user_id}")#path parameter, se declara despues de un fixed path
async def read_user(user_id: str):
    return {"user_id": user_id}

#Path parameters, parametros o variables que se pasan atraves de la ruta
@app.get("/items/{item_id}")#path:"/items/{item_id(este es el parametro)}", operation:get
async def read_item(item_id: int):#El parametro item_id pasa a la funcion como argumento, con ": int(tipo de dato)" la funcion limita el tipo de dato
    return {"item_id": item_id}

#Query parameters-base de datos
fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]

@app.get("/items/")#Se puede pasar en la ruta de manera opcional(de eta manera: ?skip=0&limit=10)para una consulta n especifico, de lo contrario mostrara lo definido en la funcion
async def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip : skip + limit]

#Metodo Post
@app.post("/items/")#path:"/items/", operation:post
async def create_item(item: Item):#Item e el modelo, agregar item a la base de datos
    return item