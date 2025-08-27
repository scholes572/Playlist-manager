from sqlalchemy import Integer, String, create_engine, Column, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base, relationship

Base = declarative_base()

class Artist(Base):
    __tablename__ = "artist"
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    genre = Column(String(50))
    debut_year = Column(Integer)

    albums = relationship("Album", back_populates="artist")

class Album(Base):
    __tablename__ = "album"
    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)
    release_year = Column(Integer)
    artist_id = Column(Integer, ForeignKey("artist.id"))

    artist = relationship("Artist", back_populates="albums")
    songs = relationship("Song", back_populates="album")   

class Song(Base):
    __tablename__ = "song"
    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)
    duration = Column(Integer)
    album_id = Column(Integer, ForeignKey("album.id"))
    album = relationship("Album", back_populates="songs")


# Database setup
# The connection string is loaded from a configuration file for better maintainability.
import configparser

config = configparser.ConfigParser()
config.read("config.ini")
db_url = config.get("database", "connection_string", fallback="sqlite:///music.db")

engine = create_engine(db_url)
Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)
session = Session()
