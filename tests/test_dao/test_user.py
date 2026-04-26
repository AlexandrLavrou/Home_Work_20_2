def test_create_user(user_dao):
    data = {
        "email": "test@example.com",
        "password": "hashed_password",
        "role": "user"
    }
    user = user_dao.create(data)

    assert user.id is not None
    assert user.email == "test@example.com"


def test_get_by_email(user_dao):
    data = {
        "email": "second@example.com",
        "password": "abc123",
        "role": "admin"
    }
    user_dao.create(data)

    user = user_dao.get_by_email("second@example.com")
    assert user is not None
    assert user.role == "admin"
