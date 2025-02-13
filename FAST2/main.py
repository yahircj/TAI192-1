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
    return {'Los usuarios registrados son': tareas}