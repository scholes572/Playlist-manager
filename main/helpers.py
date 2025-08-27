from models import session, Artist, Album, Song

#All artists helpers
def add_artist(name, genre=None, debut_year=None):
    artist = Artist(name=name, genre=genre, debut_year=debut_year)
    session.add(artist)
    session.commit()
    return artist

def list_artists():
    return session.query(Artist).all()


#All album helpers
def add_album(title, release_year, artist_id):
    album = Album(title=title, release_year=release_year, artist_id=artist_id)
    session.add(album)
    session.commit()
    return album

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
        