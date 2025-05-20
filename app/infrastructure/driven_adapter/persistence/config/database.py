import logging
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from app.application.settings import settings 
import os



SQLALCHEMY_DATABASE_URL = settings.DATABASE_URL
  
engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    pool_pre_ping=True,  # Verifica conexiones antes de usarlas
    pool_recycle=1800,   # Recicla conexiones después de 30 minutos
    pool_size=10,        # Tamaño del pool de conexiones
    max_overflow=20,     # Conexiones adicionales permitidas
    pool_timeout=30,     # Tiempo de espera máximo para obtener una conexión del pool
    connect_args={
        "connect_timeout": 10,      # Tiempo máximo de espera para conectar
        "keepalives": 1,            # Mantener conexiones vivas
        "keepalives_idle": 60,      # Tiempo de inactividad antes de enviar keepalive
        "keepalives_interval": 10,  # Intervalo entre keepalives
        "keepalives_count": 3       # Número de keepalives fallidos antes de cerrar
    }
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_session():
    session = SessionLocal()
    try:
        yield session
    except Exception:
        session.rollback()
    finally:
        session.close()
