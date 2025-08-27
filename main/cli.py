from helpers import add_artist, list_artists, add_album, list_albums, add_song, list_songs

def main():
    while True:
        print("\n🎵 Music Database CLI 🎵")
        print("1. Add Artist")
        print("2. List Artists")
        print("3. Add Album")
        print("4. List Albums")
        print("5. Add Song")
        print("6. List Songs")
        print("0. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Artist Name: ")
            genre = input("Genre: ")
            debut_year = input("Debut Year: ")
            try:
                debut_year_int = int(debut_year) if debut_year else None
            except ValueError:
                print("❌ Invalid debut year. Please enter a valid number.")
                continue
            artist = add_artist(name, genre, debut_year_int)
            print(f"✅ Added Artist: {artist.name}")

        elif choice == "2":
            artists = list_artists()
            for artist in artists:
                print(f"{artist.id}. {artist.name} ({artist.genre}, {artist.debut_year})")
            try:
                release_year_int = int(release_year)
                artist_id_int = int(artist_id)
            except ValueError:
                print("❌ Invalid release year or artist ID. Please enter valid numbers.")
                continue
            album = add_album(title, release_year_int, artist_id_int)
            print(f"✅ Added Album: {album.title}")
            title = input("Album Title: ")
            release_year = input("Release Year: ")
            artist_id = input("Artist ID: ")
            album = add_album(title, int(release_year), int(artist_id))
            try:
                duration_int = int(duration)
                album_id_int = int(album_id)
            except ValueError:
                print("❌ Invalid duration or album ID. Please enter valid numbers.")
                continue
            song = add_song(title, duration_int, album_id_int)
            print(f"✅ Added Song: {song.title}")
        elif choice == "4":
            albums = list_albums()
            for album in albums:
                print(f"{album.id}. {album.title} ({album.release_year}) - Artist ID: {album.artist_id}")

        elif choice == "5":
            title = input("Song Title: ")
            duration = input("Duration (sec): ")
            album_id = input("Album ID: ")
            song = add_song(title, int(duration), int(album_id))
            print(f"✅ Added Song: {song.title}")

        elif choice == "6":
            songs = list_songs()
            for song in songs:
                print(f"{song.id}. {song.title} ({song.duration} sec) - Album ID: {song.album_id}")

        elif choice == "0":
            print("👋 Exiting Music Database CLI...")
            break

        else:
            print("❌ Invalid choice, try again!")

if __name__ == "__main__":
    main()
        
        