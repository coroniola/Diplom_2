import pytest
import requests
from helpers import generate_random_string
from helpers import create_user_data
from constants.urls import Urls

@pytest.fixture
def create_user_and_return_data():
    data = {}
    email = f'{generate_random_string(7)}@example.com'
    name = f'{generate_random_string(8)}'
    password = f'{generate_random_string(12)}'
    data['email'] = email
    data['name'] = name
    data['password'] = password

    payload = {
        "email": email,
        "name": name,
        "password": password
    }

    response = requests.post(Urls.CREATE_USER, data=payload)
    token = response.json()['accessToken']
    data['token'] = token
    data['response'] = response

    yield data
    requests.delete(Urls.DELETE_USER, headers={'Authorization': token})



@pytest.fixture
def user_data():
    payload = create_user_data()
    response = requests.post(Urls.CREATE_USER, data=payload)

    yield payload
    token = response.json()['accessToken']
    requests.delete(Urls.DELETE_USER, headers={'Authorization': token})


@pytest.fixture
def user_token():
    payload = create_user_data()
    response = requests.post(Urls.CREATE_USER, data=payload)
    token = response.json()['accessToken']

    yield token
    requests.delete(Urls.DELETE_USER, headers={'Authorization': token})