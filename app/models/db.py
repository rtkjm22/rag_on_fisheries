from sqlalchemy import Column, Integer, String, create_engine, DateTime, func
from sqlalchemy.orm import declarative_base, sessionmaker
from pgvector.sqlalchemy import Vector
from typing import Any

DATABASE_URL = "postgresql://postgres:password@localhost:5432/rag_db"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()


class Fisheries(Base):
    __tablename__ = "fisheries"
    id = Column(Integer, primary_key=True)
    city_name = Column(String)
    content = Column(String)
    embedding: Column[Any] = Column(Vector(1024), nullable=False)
    created_at = Column(
        DateTime(timezone=True), nullable=False, server_default=func.now()
    )
    updated_at = Column(
        DateTime(timezone=True),
        nullable=False,
        server_default=func.now(),
        onupdate=func.now(),
    )


def get_session():
    return SessionLocal()
