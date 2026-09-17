from sqlalchemy import Column, Integer, String, Float, Date
from src.config.database import Base

class Gasto(Base):
    __tablename__ = "gastos"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(100), nullable=False)
    categoria = Column(String(50))
    monto = Column(Float, nullable=False)
    fecha = Column(Date, nullable=False)