from lib.music_library import MusicLibrary
from lib.track import Track

def test_no_tracks():
    library = MusicLibrary()
    assert library.all() == []

# def test_search_by_title():
#     library = MusicLibrary()
#     track1 = Track("Title_1", "Artist_1")
#     library.add(track1)
#     assert library.search_by_title("Title_1") == ["track1"]