from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# URL de conexión a la base de datos. En este ejemplo se usa SQLite,
# pero podría ser otra base de datos como PostgreSQL o MySQL.
SQLALCHEMY_DATABASE_URL = "sqlite:///./tienda_comics.sqlite"

# Crea una conexión a la base de datos.
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# Crea una clase base para tus modelos.
Base = declarative_base()

# Crea una fábrica de sesiones. Esto permitirá que, en cualquier parte
# de la aplicación, se pueda generar una sesión que está conectada al engine.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
