from datetime import datetime
from models.user import User, UserDAO
from models.song import Song, SongDAO


def print_objs(objs: list):
    for obj in objs:
        print(obj)
    print()


def test_user_dao():
    UserDAO.clear()

    user1 = User(
        id=0,
        name="John Doe",
        password="password123",
        creation_date=datetime.now(),
        is_admin=6,
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
    updated_user.set_name("John Updated")
    updated_user.set_password("newpassword")
    updated_user.set_is_admin(True)
    UserDAO.update(updated_user.id, updated_user)
    print("Updated user with ID 1:")
    print_objs(UserDAO.get())

    UserDAO.delete(2)
    print("Deleted user with ID 2:")
    print_objs(UserDAO.get())


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
        updated_song.set_title("Bohemian Rhapsody (Remastered)")
        updated_song.set_artist("Queen Remastered")
        updated_song.set_count(100)
        SongDAO.update(updated_song.id, updated_song)
        print("Updated song with ID 1:")
        print_objs(SongDAO.get())

    SongDAO.delete(2)
    print("Deleted song with ID 2:")
    print_objs(SongDAO.get())


if __name__ == "__main__":
    print("\n\n\tTesting Users:")
    UserDAO.load()
    test_user_dao()

    print("\n\n\tTesting Songs:")
    SongDAO.load()
    test_song_dao()
