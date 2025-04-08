import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Nombre de la base de datos (puedes cambiarlo según lo necesites)
dbName = "tienda_comics.sqlite"

# Ruta absoluta del directorio actual (carpeta DB)
base_dir = os.path.dirname(os.path.realpath(__file__))

# URL completa del archivo SQLite
dbURL = f"sqlite:///{os.path.join(base_dir, dbName)}"

# Crear motor de conexión con SQLAlchemy
engine = create_engine(dbURL, connect_args={"check_same_thread": False}, echo=True)

# Crear la fábrica de sesiones (si se necesita en otros módulos)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base declarativa para modelos ORM
Base = declarative_base()
