import os
import sys
import pytest
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))
from app import create_app
from uuid import uuid4
from database import DatabaseManipulator


@pytest.fixture
def app():
    app = create_app()
    app.config.update({'testing': True}, )
    yield app


@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture
def runner(app):
    return app.test_cli_runner()

@pytest.fixture
def user_id():
    return str(uuid4())

@pytest.fixture
def user_data():
    return {'ingredients':['Жарена картопля', 'Фарш з макаронами', 'Пельмені']}

@pytest.fixture
def recommended_ingredients():
    return ['Банани', 'Макарони', 'Сир']

@pytest.fixture
def db():
    db_instance = DatabaseManipulator(test_db=True)
    yield db_instance

    db_instance.db.drop_collection('user')