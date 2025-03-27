from fastapi import FastAPI, HTTPException
from modelsPydantic import modeloUsuario, modeloAuth
from genToken import createToken
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from middlewares import BearerJWT
from DB.conexion import Session
from models.modelsDB import User
from fastapi import APIRouter

routerUsuario = APIRouter()


#Endpoint Buscar un usuario por ID
@routerUsuario.get('/usuarioID/{id}',response_model=modeloUsuario,  tags=['Operaciones CRUD'])
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



#Endpoint consultar todos los usuarios
@routerUsuario.get('/todosUsuarios',  response_model=modeloUsuario, tags=['Operaciones CRUD'])
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
@routerUsuario.post("/usuarios", response_model=modeloUsuario, tags=["Operaciones CRUD"])
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
@routerUsuario.put('/usuariosPut/{id}', response_model=modeloUsuario, tags=['Operaciones CRUD'])
def actualizar_usuario(id: int, usuarioActualizado: modeloUsuario):
    db = Session()
    try:
        usuario = db.query(User).filter(User.id == id).first()

        if not usuario:
            raise HTTPException(status_code=404, detail="Usuario no encontrado.")

        
        for key, value in usuarioActualizado.model_dump().items():
            setattr(usuario, key, value)

        db.commit()
        db.refresh(usuario)  

        return usuario

    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={"message": "Error al actualizar el usuario.", "Excepción": str(e)}
        )
    finally:
        db.close()


# Endpoint - Eliminar usuario
@routerUsuario.delete('/usuarioDelete/{id}', tags=['Operaciones CRUD'])
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