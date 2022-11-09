from fastapi import FastAPI

#instancia
app = FastAPI()

#path-operations-functions
#Metodos get

#Ruta root-ruta principal
@app.get("/") #path:"/", operation:get
async def root(): #function: root() [corresponde a la funcion que se encuentra debajo del decorador]
    return {"message": "Hello World"}

#Path parameters, parametros o variables que se pasan atraves de la ruta
@app.get("/items/{item_id}")#path:"/items/{item_id(este es el parametro)}", operation:get
async def read_item(item_id: int):#El parametro item_id pasa a la funcion como argumento, con ": int(tipo de dato)" la funcion limita el tipo de dato
    return {"item_id": item_id}