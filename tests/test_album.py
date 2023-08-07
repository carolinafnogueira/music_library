from lib.album import *

'''
Album constructs with id, title, release_year, and artist_id
'''

def test_album_construct():
    album = Album(1,'Test Title', 1980, 1)
    assert album.id == 1
    assert album.title == 'Test Title'
    assert album.release_year == 1980
    assert album.artist_id == 1

'''
We can format albums to strings nicely
'''

def test_albums_format_nicely():
    album = Album(1, 'Doolittle', 1989, 1)
    assert str(album) == Album(1, 'Doolittle', 1989, 1)