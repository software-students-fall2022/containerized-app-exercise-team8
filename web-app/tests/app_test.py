import pytest
from ..app import app

# test route "/" with GET


def test_route():
    url = '/'
    response = app.get(url)
    assert response.status_code == 200

# test a fake route


def test_fakeRoute():
    url = '/fakeRoute'
    response = app.get(url)
    assert response.status_code == 404
