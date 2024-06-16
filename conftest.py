import pytest
import requests
from helpers import generate_random_string, create_user_data
from constants.urls import Urls

@pytest.fixture
def user_data():
    payload = create_user_data()
    response = requests.post(Urls.CREATE_USER, data=payload)
    token = response.json()['accessToken']
    data = {
        'email': payload['email'],
        'name': payload['name'],
        'password': payload['password'],
        'token': token,
        'response': response
    }
    yield data
    requests.delete(Urls.DELETE_USER, headers={'Authorization': token})
