from datetime import datetime
from models.user import User, UserDAO
from models.song import Song, SongDAO
from models.playlist import Playlist, PlaylistDAO
from models.library import Library, LibraryDAO
from models.play_count import PlayCount, PlayCountDAO
from models.playlist_item import PlaylistItem, PlaylistItemDAO


def print_objs(objs: list):
    for obj in objs:
        print(obj)
    print()


def test_library_dao():
    LibraryDAO.clear()

    library1 = Library(
        id=0,
        is_global=True,
        folder="/music/global",
    )
    library2 = Library(
        id=0,
        is_global=False,
        folder="/music/user1",
    )

    LibraryDAO.insert(library1)
    LibraryDAO.insert(library2)
    print("Inserted libraries:")
    print_objs(LibraryDAO.get())

    retrieved_library = LibraryDAO.get_by_id(1)
    print(f"Retrieved library with ID 1:\n{retrieved_library}\n")

    updated_library = LibraryDAO.get_by_id(1)
    if updated_library:
        updated_library.is_global = False
        updated_library.folder = "/music/updated"
        LibraryDAO.update(updated_library.id, updated_library)
        print("Updated library with ID 1:")
        print_objs(LibraryDAO.get())

    LibraryDAO.delete(2)
    print("Deleted library with ID 2:")
    print_objs(LibraryDAO.get())


def test_play_count_dao():
    PlayCountDAO.clear()

    play_count1 = PlayCount(
        id=0,
        id_user=1,
        id_song=1,
        count=10,
    )
    play_count2 = PlayCount(
        id=0,
        id_user=2,
        id_song=2,
        count=5,
    )

    PlayCountDAO.insert(play_count1)
    PlayCountDAO.insert(play_count2)
    print("Inserted play counts:")
    print_objs(PlayCountDAO.get())

    retrieved_play_count = PlayCountDAO.get_by_id(1)
    print(f"Retrieved play count with ID 1:\n{retrieved_play_count}\n")

    updated_play_count = PlayCountDAO.get_by_id(1)
    if updated_play_count:
        updated_play_count.count = 20
        PlayCountDAO.update(updated_play_count.id, updated_play_count)
        print("Updated play count with ID 1:")
        print_objs(PlayCountDAO.get())

    PlayCountDAO.delete(2)
    print("Deleted play count with ID 2:")
    print_objs(PlayCountDAO.get())


def test_playlist_item_dao():
    PlaylistItemDAO.clear()

    playlist_item1 = PlaylistItem(
        id=0,
        id_playlist=1,
        id_song=1,
        count=3,
    )
    playlist_item2 = PlaylistItem(
        id=0,
        id_playlist=2,
        id_song=2,
        count=1,
    )

    PlaylistItemDAO.insert(playlist_item1)
    PlaylistItemDAO.insert(playlist_item2)
    print("Inserted playlist items:")
    print_objs(PlaylistItemDAO.get())

    retrieved_playlist_item = PlaylistItemDAO.get_by_id(1)
    print(f"Retrieved playlist item with ID 1:\n{retrieved_playlist_item}\n")

    updated_playlist_item = PlaylistItemDAO.get_by_id(1)
    if updated_playlist_item:
        updated_playlist_item.count = 5
        PlaylistItemDAO.update(updated_playlist_item.id, updated_playlist_item)
        print("Updated playlist item with ID 1:")
        print_objs(PlaylistItemDAO.get())

    PlaylistItemDAO.delete(2)
    print("Deleted playlist item with ID 2:")
    print_objs(PlaylistItemDAO.get())


def test_playlist_dao():
    PlaylistDAO.clear()

    playlist1 = Playlist(
        id=1,
        id_user=1,
        name="Chill Vibes",
        description="A relaxing playlist for studying.",
        creation_date=datetime.now(),
    )
    playlist2 = Playlist(
        id=2,
        id_user=2,
        name="Workout Mix",
        description="High-energy songs for workouts.",
        creation_date=datetime.now(),
    )

    PlaylistDAO.insert(playlist1)
    PlaylistDAO.insert(playlist2)
    print("Inserted playlists:")
    print_objs(PlaylistDAO.get())

    retrieved_playlist = PlaylistDAO.get_by_id(1)
    print(f"Retrieved playlist with ID 1:\n{retrieved_playlist}\n")

    updated_playlist = PlaylistDAO.get_by_id(1)
    updated_playlist.name = "Chill Vibes Updated"
    updated_playlist.description = "An updated relaxing playlist."
    PlaylistDAO.update(updated_playlist.id, updated_playlist)
    print("Updated playlist with ID 1:")
    print_objs(PlaylistDAO.get())

    PlaylistDAO.delete(2)
    print("Deleted playlist with ID 2:")
    print_objs(PlaylistDAO.get())


def test_song_dao():
    SongDAO.clear()

    song1 = Song(
        id=0,
        id_library=1,
        title="Bohemian Rhapsody",
        artist="Queen",
        genre="Rock",
        file="bohemian_rhapsody.mp3",
        count=0,
    )
    song2 = Song(
        id=0,
        id_library=1,
        title="Shape of You",
        artist="Ed Sheeran",
        genre="Pop",
        file="shape_of_you.mp3",
        count=0,
    )

    SongDAO.insert(song1)
    SongDAO.insert(song2)
    print("Inserted songs:")
    print_objs(SongDAO.get())

    retrieved_song = SongDAO.get_by_id(1)
    print(f"Retrieved song with ID 1:\n{retrieved_song}\n")

    updated_song = SongDAO.get_by_id(1)
    if updated_song:
        updated_song.title = "Bohemian Rhapsody (Remastered)"
        updated_song.artist = "Queen Remastered"
        updated_song.count = 100
        SongDAO.update(updated_song.id, updated_song)
        print("Updated song with ID 1:")
        print_objs(SongDAO.get())

    SongDAO.delete(2)
    print("Deleted song with ID 2:")
    print_objs(SongDAO.get())


def test_user_dao():
    UserDAO.clear()

    user1 = User(
        id=0,
        name="John Doe",
        password="password123",
        creation_date=datetime.now(),
        is_admin=False,
    )
    user2 = User(
        id=0,
        name="Jane Smith",
        password="securepassword",
        creation_date=datetime.now(),
        is_admin=True,
    )

    UserDAO.insert(user1)
    UserDAO.insert(user2)
    print("Inserted users:")
    print_objs(UserDAO.get())

    retrieved_user = UserDAO.get_by_id(1)
    print(f"Retrieved user with ID 1:\n{retrieved_user}\n")

    updated_user = UserDAO.get_by_id(1)
    updated_user.name = "John Updated"
    updated_user.password = "newpassword"
    updated_user.is_admin = True
    UserDAO.update(updated_user.id, updated_user)
    print("Updated user with ID 1:")
    print_objs(UserDAO.get())

    UserDAO.delete(2)
    print("Deleted user with ID 2:")
    print_objs(UserDAO.get())


if __name__ == "__main__":
    print("\n\n\tTesting Libraries:")
    LibraryDAO.load()
    test_library_dao()

    print("\n\n\tTesting Play Counts:")
    PlayCountDAO.load()
    test_play_count_dao()

    print("\n\n\tTesting Playlist Items:")
    PlaylistItemDAO.load()
    test_playlist_item_dao()

    print("\n\n\tTesting Playlists:")
    PlaylistDAO.load()
    test_playlist_dao()

    print("\n\n\tTesting Songs:")
    SongDAO.load()
    test_song_dao()

    print("\n\n\tTesting Users:")
    UserDAO.load()
    test_user_dao()
