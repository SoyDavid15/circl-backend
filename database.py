import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
# 1. IMPORTANTE: Agrega 'declarative_base' y 'sessionmaker' aquí arriba
from sqlalchemy.orm import declarative_base, sessionmaker 
from sqlalchemy.pool import NullPool

# Load environment variables from .env
load_dotenv()

# Fetch variables
USER = os.getenv("user")
PASSWORD = os.getenv("password")
HOST = os.getenv("host")
PORT = os.getenv("port")
DBNAME = os.getenv("dbname")

# Construct the SQLAlchemy connection string
DATABASE_URL = f"postgresql+psycopg2://{USER}:{PASSWORD}@{HOST}:{PORT}/{DBNAME}?sslmode=require"

# Tip de Supabase: Descomenta el NullPool para que no choque con su sistema de conexiones externo
engine = create_engine(DATABASE_URL, poolclass=NullPool)

# === 2. LO QUE TE HACÍA FALTA: AGREGAR ESTAS LÍNEAS ===

# Crea la fábrica de sesiones para interactuar con las tablas
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Crea el 'Base' con B mayúscula que tu main.py está intentando importar
Base = declarative_base()

# Crea la función 'get_db' que tu main.py necesita para abrir/cerrar conexiones
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# ======================================================

# Test the connection (Tu código de prueba original)
try:
    with engine.connect() as connection:
        print("Connection successful!")
except Exception as e:
    print(f"Failed to connect: {e}")