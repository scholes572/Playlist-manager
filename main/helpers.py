from models import session, Artist, Album, Song

#All artists helpers
def add_artist(name, genre=None, debut_year=None):
    try:
        artist = Artist(name=name, genre=genre, debut_year=debut_year)
        session.add(artist)
        session.commit()
        return artist
    except Exception as e:
        session.rollback()
        print(f"Error adding artist: {e}")
        return None

def add_album(title, release_year, artist_id):
    try:
        album = Album(title=title, release_year=release_year, artist_id=artist_id)
        session.add(album)
        session.commit()
        return album
    except Exception as e:
        session.rollback()
        print(f"Error adding album: {e}")
        return None
# Removed duplicate and incomplete function definition

def list_albums():
    return session.query(Album).all()


#all Song helpers
def add_song(title, duration, album_id):
    song = Song(title=title, duration=duration, album_id=album_id)
    session.add(song)
    session.commit()
    return song 

def list_songs():
    return session.query(Song).all()
        