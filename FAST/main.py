from fastapi import FastAPI, HTTPException
from typing import Optional
#se definen 3 parametros
app= FastAPI(
    title='mi primerAPI 192',
    description='christian montalvo moreno',
    version='1.0.1'
)
usuarios = [
    {"id": 1, "nombre":"christian", "edad":25},
    {"id": 2, "nombre":"uriel", "edad":22},
    {"id": 3, "nombre":"luis", "edad":21},
    {"id": 4, "nombre":"toño", "edad":20},
    {"id": 5, "nombre":"samu", "edad":14}
    
]

#Endpoint home
@app.get('/', tags=['hola mundo'])
def home():
    return {'hello':'world FastAPI'}

    #Endpoint consultas todos
@app.get('/todosUsuarios/', tags=['Operaciones CRUD'])
def leerUsuario():
    return {'Los usuarios registrados son': usuarios}

        #Endpoint agregar nuevo
@app.post('/usuario/', tags=['Operaciones CRUD'])
def agregarUsuario(usuario:dict):
    for usr in usuarios:
        if usr["id"] == usuario.get("id"):
            raise HTTPException(status_code=400, detail="el id ya exite")
    usuarios.append(usuario)
    return usuario

        #Endpoint actualizar
@app.put('/usuario/{id}', tags=['Operaciones CRUD'])
def actualizar(id:int,usuarioActualizado:dict):
    for index, usr in enumerate(usuarios):
        if usr["id"] == id:
           usuarios[index].update(usuarioActualizado)
           return usuarios[index]
    raise HTTPException(status_code=404, detail="usuario no encontrado")
    
   #Endpoint eliminar
@app.delete('/usuario/{id}', tags=['Operaciones CRUD'])
def eliminar(id:int):
    for index, usr in enumerate(usuarios):
        if usr["id"] == id:
           usuarios.pop(index)
           return {"usuario eliminado"}
    raise HTTPException(status_code=404, detail="usuario no encontrado")





