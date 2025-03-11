from fastapi import HTTPException, Request 
from fastapi.security import HTTPBearer 
from genToken import validateToken 

class BearerJWT(HTTPBearer):
    async def _call_(self, request: Request):
        auth = await super()._call_(request)
        data = validateToken(auth.credentials)

        if not isinstance(data, dict): # Verificar si es un diccionario válido 
            raise HTTPException(status_code=401, detail="Formato de Token no inválido")
        
        if data.get('email')!= 'christian@example.com': # Usar .get() para evitar KeyError 
            raise HTTPException(status_code=403, detail="Credenciales no válidas")