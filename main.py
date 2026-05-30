from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from pydantic import BaseModel
from datetime import datetime
from typing import Optional

# 1. Importamos la conexión y el Base desde tu nuevo archivo database.py
from database import engine, Base, get_db

# 2. Importamos tu modelo de incidentes desde models.py
from models import Incidente

# 3. Esto crea la tabla 'incidentes' en Supabase de forma automática si no existe
Base.metadata.create_all(bind=engine)

# 4. Inicializamos FastAPI
app = FastAPI(title="API de Seguridad Local - MVP Colombia")

# 5. ESQUEMA DE PYDANTIC: Valida los datos que entran cuando publicas a mano
class IncidenteCreate(BaseModel):
    barrio: str
    tipo_delito: str
    fecha_y_hora: datetime  # Acepta formatos como "2026-05-27 15:30:00"
    peso: int = 1
    carrera: Optional[int] = None
    calle: Optional[int] = None

# 6. ENDPOINT POST: El que usarás para enviar los datos de seguridad a Supabase
@app.post("/api/incidentes", status_code=status.HTTP_201_CREATED)
def guardar_incidente(incidente_in: IncidenteCreate, db: Session = Depends(get_db)):
    try:
        # Mapeamos el JSON recibido al modelo de la base de datos de SQLAlchemy
        nuevo_incidente = Incidente(
            barrio=incidente_in.barrio,
            tipo_delito=incidente_in.tipo_delito,
            fecha_y_hora=incidente_in.fecha_y_hora,
            peso=incidente_in.peso,
            carrera=incidente_in.carrera,
            calle=incidente_in.calle
        )
        
        # Guardamos la información en Supabase
        db.add(nuevo_incidente)
        db.commit()
        db.refresh(nuevo_incidente) # Nos devuelve el ID autogenerado por la BD
        
        return {
            "status": "success",
            "message": "Incidente de seguridad registrado correctamente",
            "id_incidente": nuevo_incidente.id
        }
        
    except Exception as e:
        db.rollback() # Si algo sale mal, cancela la operación para no corromper datos
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, 
            detail=f"Error al guardar en Supabase: {str(e)}"
        )

# Endpoint básico para verificar que tu API responde en la web
@app.get("/")
def read_root():
    return {"message": "¡API de seguridad corriendo y conectada a Supabase exitosamente!"}