from sqlalchemy import String, Integer, DateTime, func
from sqlalchemy.orm import Mapped, mapped_column
from database import Base # Asegúrate de que apunte a tu clase Base

class Incidente(Base):
    __tablename__ = "incidentes"

    # ID autoincremental
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    
    # Fecha de creación del registro en la base de datos (se llena sola)
    created_at: Mapped[DateTime] = mapped_column(DateTime, server_default=func.now())
    
    # Información del lugar y tipo de delito (reemplaza varchar por String)
    barrio: Mapped[str] = mapped_column(String(100), nullable=False)
    incidente: Mapped[str] = mapped_column(String(100), nullable=False)
    
    # Fecha y hora exacta en la que ocurrió el incidente real
    fecha_y_hora: Mapped[DateTime] = mapped_column(DateTime, nullable=False)
    
    # Gravedad o peso del delito (ej: 1 al 10)
    peso: Mapped[int] = mapped_column(Integer, default=1)
    
    # Direcciones aproximadas (pueden ser nulas por si la noticia no da el dato exacto)
    carrera: Mapped[int] = mapped_column(Integer, nullable=True)
    calle: Mapped[int] = mapped_column(Integer, nullable=True)