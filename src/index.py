from datetime import datetime
from models.user import User, UserDAO


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
    updated_user.set_name("John Updated")
    updated_user.set_password("newpassword")
    updated_user.set_is_admin(True)
    UserDAO.update(updated_user.get_id(), updated_user)
    print("Updated user with ID 1:")
    print_objs(UserDAO.get())

    UserDAO.delete(2)
    print("Deleted user with ID 2:")
    print_objs(UserDAO.get())


if __name__ == "__main__":
    UserDAO.load()
    test_user_dao()
