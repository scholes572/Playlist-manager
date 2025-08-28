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



def get_albums_by_artist(artist_id):
    """Return all albums for a given artist ID"""
    artist = session.query(Artist).get(artist_id)
    if artist:
        return artist.albums
    return None

def get_songs_by_album(album_id):
    """Return all songs for a givem album ID"""
    album = session.query(Album).get(album_id)
    if album:
        return album.songs
    return None