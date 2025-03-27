from fastapi import FastAPI, HTTPException, Depends
from typing import Optional, List
from modelsPydantic import modeloUsuario, modeloAuth
from genToken import createToken
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from middlewares import BearerJWT
from DB.conexion import Session, engine, Base
from models.modelsDB import User



app = FastAPI(
    title="Mi primer API 192",
    description="Christian MONTALVO, primeros pasos en fastAPI",
    version='1.0.1'
)


Base.metadata.create_all(bind = engine)


# BD ficticia
usuarios = [
        {"id":1, "nombre":"chris", "edad":25, "correo":"chris@gmail.com"},
        {"id":2, "nombre":"monse", "edad":21, "correo":"mon@gmail.com"},
        {"id":3, "nombre":"antonio", "edad":20, "correo":"toño@gmail.com"},
        {"id":4, "nombre":"uri", "edad":20, "correo":"uri@gmail.com"},
]



#Endpoint home
@app.get('/', tags=['Hola mundo'])
def home():
    return {'hello':'world fastAPI'}



# Endpoint Autenticación
@app.post('/auth/', tags=['Autentificación'])
def login(autorización:modeloAuth):
    if autorización.email == 'christian@example.com' and autorización.passw == '12345678':
        token:str = createToken(autorización.model_dump())
        print(token)
        return JSONResponse(content=token)
    else:
        return {"Aviso":"El usuario no está autorizado."}



#Endpoint Buscar un usuario por su ID
@app.get('/usuarioID/{id}',response_model=modeloUsuario,  tags=['Operaciones CRUD'])
def buscarUno(id: int):
    db=Session()
    try:
        consultauno = db.query(User).filter(User.id == id).first()

        if not consultauno:
            return JSONResponse(status_code=404, content={'message':'Usuario no encontrado.'})
        return JSONResponse(content=jsonable_encoder(consultauno))
    
    except Exception as e:
        return JSONResponse(status_code=500, 
                            content={'message':'Error al consultar usuario.', 
                                     'Excepción':str(e)})
    finally:
        db.close()



#Endpoint CONSULTA TODOS
# @app.get('/todosUsuarios', dependencies=[Depends(BearerJWT())], response_model = List[modeloUsuario], tags=['Operaciones CRUD'])
@app.get('/todosUsuarios',  response_model=modeloUsuario, tags=['Operaciones CRUD'])
def leerUsuarios():
    db=Session()
    try:
        consulta = db.query(User).all()
        return JSONResponse(content=jsonable_encoder(consulta))
    except Exception as e:
        return JSONResponse(status_code=500, 
                            content={'message':'Error al consultar usuarios.', 
                                     'Excepción':str(e)})
    finally:
        db.close()



# Endpoint - Agregar nuevos usuarios
""" @app.post('/usuarios/', response_model=modeloUsuario, tags = ['Operaciones CRUD'])
def agregarUsuario(usuario:modeloUsuario):
    db = Session()
    try:
        nuevo_usuario = User(**usuario.model_dump())
        db.add(nuevo_usuario)
        db.commit()
        return JSONResponse(status_code=201, 
                            content={'message':'Usuario guardado.', 
                            'usuario':usuario.model_dump()  })
    except Exception as e:
        db.rollback()
        return JSONResponse(status_code=500, 
                            content={'message':'Error al guardar usuario.', 
                                     'Excepción':str(e)})
    finally:
        db.close()
 """
@app.post("/usuarios", response_model=modeloUsuario, tags=["Operaciones CRUD"])
def agregar_usuario(usuario: modeloUsuario):
    """Agrega un nuevo usuario a la base de datos."""
    db = Session()
    try:
        nuevo_usuario = User(**usuario.model_dump())
        db.add(nuevo_usuario)
        db.commit()
        return JSONResponse(status_code=201, content={"message": "Usuario Guardado", "usuario": usuario.model_dump()})
    except Exception as e:
        db.rollback()
        return JSONResponse(status_code=500, content={"message": "Error al guardar usuario", "Exception": str(e)})
    finally:
        db.close()

# Endpoint - Modificar usuario
@app.put('/usuariosPut/{id}', response_model=modeloUsuario, tags=['Operaciones CRUD'])
def actualizar_usuario(id: int, usuarioActualizado: modeloUsuario):
    db = Session()
    try:
        usuario = db.query(User).filter(User.id == id).first()

        if not usuario:
            raise HTTPException(status_code=404, detail="Usuario no encontrado.")

        # Actualizamos los atributos del modelo
        for key, value in usuarioActualizado.model_dump().items():
            setattr(usuario, key, value)

        db.commit()
        db.refresh(usuario)  # Refresca para obtener los datos actualizados

        return usuario

    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={"message": "Error al actualizar el usuario.", "Excepción": str(e)}
        )
    finally:
        db.close()


# Endpoint - Eliminar usuario
@app.delete('/usuarioDelete/{id}', tags=['Operaciones CRUD'])
def eliminar_usuario(id: int):
    db = Session()
    try:
        usuario = db.query(User).filter(User.id == id).first()

        if not usuario:
            return JSONResponse(status_code=404, content={'message': 'Usuario no encontrado.'})
        
        db.delete(usuario)
        db.commit()
        return JSONResponse(content={'message': 'Usuario eliminado exitosamente.'})

    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={'message': 'Error al eliminar usuario.', 'Excepción': str(e)}
        )
    finally:
        db.close()