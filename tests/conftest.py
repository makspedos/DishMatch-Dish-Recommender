import os
import sys
from app import create_app

import pytest

@pytest.fixture()
def app():
    app = create_app()
    app.config.update({'testing':True},)
    yield app

@pytest.fixture()
def client(app):
    return app.test_client()

@pytest.fixture()
def runner(app):
    return app.test_cli_runner()



