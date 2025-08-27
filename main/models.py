from sqlalchemy import Interger, String, Text, Date, ForeignKey, create_engine, column
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

Base = declarative_base()

class Artist(Base):
    __tablename__ = "artist"
    id = column(Interger, primary_key=True)
    name = column(String(100), nullable=False)
    genre = column(String(50))
    debut_year = column(Interger)


    # relationships
    albums = relationship("Album", back_populates="artist")
    songs = relationship("Song", back_populates="album")


class Album(Base):
    __tablename__ = "album"
    id = column(Interger, primary_key=True)
    title = column(String(100), nullable=False)
    release_year = column(Interger)
    artist_id = column(Interger, ForeignKey("artist"))

    #relationships
    artist = relationship("Artist", back_populates="albums")
    songs = relationship("Song", back_populates="album")


class Song(Base):
    __tablename__ = "song"
    id = column(Interger, primary_key=True)
    title  = column(String(100), nullable=False)
    duration = column(Interger, ForeignKey("album.id"))

    #relationships 
    album = relationship("Album", back_populates="songs")


engine = create_engine("sqlite:///music.db") 
Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)
session = Session()