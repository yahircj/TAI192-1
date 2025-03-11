from pydantic import BaseModel, Field, EmailStr

# Modelo
class Usuario(BaseModel):
    id: int = Field(..., gt=0, description="ID único y solo positivos")
    nombre: str = Field(..., min_length=3, max_length=85, description="Solo letras: mínimo 3, máximo 85 caracteres")
    edad: int = Field(..., gt=0, description="Edad debe ser un número positivo y realista")
    correo: EmailStr = Field(..., description="Debe ser un correo electrónico válido", example="correo@example.com")
    #gt mayor que
    #ge mayor o igual
    #lt menor que 
    #le menor o igual que


class modeloAuth(BaseModel):
     email: EmailStr = Field(..., description="Debe ser un correo electrónico válido", example="correo@example.com")
     passw: str= Field(..., min_length=8, strip_whitespace=True,description="contraseña minimo 8 caracteres")
