from fastapi import FastAPI
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
#endpoitpromedio
@app.get('/promedio', tags=['Mi calificacion TAI'])
def promedio():
    return 6.1

#endpoit parametro obligatorio
@app.get('/usuario/{id}', tags=['parametro obligatorio'])
def consultaUsuarioo(id:int):
    #conectamos a la BD
    #consultamos
    return {'se encontro el usuario':id}

#endpoint con varios parametro opcionales
@app.get("/usuarios/", tags=["3 parámetros opcionales"])
async def consulta_usuarios(
    usuario_id: Optional[int] = None,
    nombre: Optional[str] = None,
    edad: Optional[int] = None
):
    resultados = []

    for usuario in usuarios:
        if (
            (usuario_id is None or usuario["id"] == usuario_id) and
            (nombre is None or usuario["nombre"].lower() == nombre.lower()) and
            (edad is None or usuario["edad"] == edad)
        ):
            resultados.append(usuario)

    if resultados:
        return {"usuarios_encontrados": resultados}
    else:
        return {"mensaje": "No se encontraron usuarios que coincidan con los parámetros proporcionados."}
