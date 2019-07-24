import pytest
from app import create_app


@pytest.fixture(scope='module')
def new_user():
    user = User('test', 'test@gmail.com', '123456')
    return user


@pytest.fixture(scope='module')
def test_client():
    flask_app = create_app()

    testing_client = flask_app.test_client()

    ctx = flask_app.app_context()
    ctx.push()

    yield testing_client

    ctx.pop()


@pytest.fixture(scope='module')
def init_database():

    #db.create_all()

    # Insert user data
    user1 = User(email='patkennedy79@gmail.com', plaintext_password='FlaskIsAwesome')
    user2 = User(email='kennedyfamilyrecipes@gmail.com', plaintext_password='PaSsWoRd')
    #db.session.add(user1)
    #db.session.add(user2)

    # Commit the changes for the profile
    #db.session.commit()

    #yield db  # this is where the testing happens!

    #db.drop_all()