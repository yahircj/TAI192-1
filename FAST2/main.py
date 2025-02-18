from fastapi import FastAPI, HTTPException
from typing import Optional
#parametros de mi segunda api
app= FastAPI(
    title='mi segundaAPI 192',
    description='christian montalvo moreno',
    version='2.0.1'
    )

tareas = [
    {
        "id": 1,
        "titulo": "Estudiar para el examen",
        "descripcion": "Repasar los apuntes de TAI ",
        "vencimiento": "14-02-24",
        "Estado": "completada"
    }
]

    #Endpoint consultas todos
@app.get('/todaslasTareas/', tags=['Operaciones CRUD'])
def leerTareas():
    return {'Las tareas registradas son': tareas}

            #Endpoint agregar nueva tarea
@app.post('/tarea/', tags=['Operaciones CRUD'])
def agregarTarea(tarea:dict):
    for usr in tareas:
        if usr["id"] == tarea.get("id"):
            raise HTTPException(status_code=400, detail="el id ya exite")
    tareas.append(tarea)
    return tarea

     #Endpoint actualizar tareas
@app.put('/tarea/{id}', tags=['Operaciones CRUD'])
def actualizar(id:int,tareaActualizada:dict):
    for index, usr in enumerate(tareas):
        if usr["id"] == id:
           tareas[index].update(tareaActualizada)
           return tareas[index]
    raise HTTPException(status_code=404, detail="tarea no encontrada")
    
   #Endpoint eliminar
@app.delete('/tarea/{id}', tags=['Operaciones CRUD'])
def eliminar(id:int):
    for index, usr in enumerate(tareas):
        if usr["id"] == id:
           tareas.pop(index)
           return {"tarea eliminada"}
    raise HTTPException(status_code=404, detail="tarea no encontrada")