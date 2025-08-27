from models import session, Artist, Album, Song

def add_artist(name, genre, debut_year):
    new_artist = Artist(name=name, genre=genre, debut_year=debut_year)
    session.add(new_artist)
    session.commit()

def add_album(title, release_year, artist_id):
    new_album = Album(title=title, release_year=release_year, artist_id=artist_id)
    session.add(new_album)
    session.commit()

def add_song(title,duration, album_id):
    new_song = Song(title=title, duration=duration, album_id=album_id)
    session.add(new_song)
    session.commit()
        

def list_artists():
    return session.query(Artist).all()
def list_albums():
    return session.query(Album).all()
def list_songs():
    return session.query(Song).all()  