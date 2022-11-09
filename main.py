from fastapi import FastAPI

#instancia
app = FastAPI()

#path-operations-functions
#Metodos get

#Ruta root
@app.get("/") #path:"/", operation:get
async def root(): #function: root() [corresponde a la funcion que se encuentra debajo del decorador]
    return {"message": "Hello World"}