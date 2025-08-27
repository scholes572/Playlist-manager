from sqlalchemy import Interger, String, Text, Date, ForeignKey, create_engine, column
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

Base = declarative_base()

class Artist(Base):
    __tablename__ = "artist"
    id = column(Interger, primary_key=True)
    name = column(String(100), nullable=False)
    genre = column(String(50))
    debut_year = column(Interger)

    albums = relationship("Album", back_populates="artist")
    songs = relationship("Song", back_populates="album")
