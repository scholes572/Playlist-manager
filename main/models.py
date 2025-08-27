from sqlalchemy import Integer, String, create_engine, Column, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base, relationship

Base = declarative_base()

class Artist(Base):
    __table__ = "artist"
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    genre = Column(String(50))
    debut_year = Column(Integer)

    albums = relationship("Album", back_populates="artist")