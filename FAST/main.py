from fastapi import FastAPI
from DB.conexion import  engine, Base
from routers.usuario import routerUsuario
from routers.auth import routerAuth



app = FastAPI(
    title="Mi primer API 192",
    description="Christian MONTALVO, primeros pasos en fastAPI",
    version='1.0.1'
)


Base.metadata.create_all(bind = engine)


#Endpoint home
@app.get('/', tags=['Hola mundo'])
def home():
    return {'hello':'world fastAPI'}

app.include_router(routerUsuario)
app.include_router(routerAuth)



