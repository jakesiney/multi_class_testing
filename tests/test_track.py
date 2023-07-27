from lib.track import Track

def test_build_track_and_return_track_and_title():
    track = Track("Title_1", "Artist_1")
    assert track.title == ("Title_1")
    assert track.artist == ("Artist_1")

