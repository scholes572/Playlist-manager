from models import session, Artist, Album, Song

def add_artist(name, genre=None, debut_year=None):
    artist = Artist(name=name, genre=genre, debut_year=debut_year)
    session.add(artist)
    session.commit()
    return artist

def list_artists():
    return session.query(Artist).all()

