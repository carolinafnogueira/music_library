from lib.database_connection import DatabaseConnection
from lib.artist_repository import ArtistRepository
from lib.album_repository import AlbumRepository


# Connect to the database
connection = DatabaseConnection()
connection.connect()

# Seed with some seed data
connection.seed("seeds/music_library.sql")

# Run the application
print('''
      Welcome to music library manager\033[31m!\033[m
      
      What would you like to do\033[31m?\033[m
      [1] List all albums
      [2] List all artists
      ''')
users_choice = int(input('Enter your choice: '))

if users_choice == 1:
    print('\nHere is the list of albums:\n')
    album_repo = AlbumRepository(connection)
    albums = album_repo.all()
    for album in albums:
        print(f"\033[31m*\033[m {album.id:2} - {album.title}")
elif users_choice == 2:
    print('\nHere is the list of artists:\n')
    artist_repo = ArtistRepository(connection)
    artists = artist_repo.all()
    for artist in artists:
        print(f"\033[31m*\033[m {artist.id:2} - {artist.name}")


# # Retrieve all artists
# artist_repository = ArtistRepository(connection)
# artists = artist_repository.all()

# # List them out
# for artist in artists:
#     print(artist)

# album_repository = AlbumRepository(connection)
# albums = album_repository.all()

# for album in albums:
#     print(album)

# # Find a single album
# album_repo = AlbumRepository(connection)
# album = album_repo.find(5)

# # Show the album selected
# print(album)



