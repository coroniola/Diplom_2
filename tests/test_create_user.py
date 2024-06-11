import pytest
import requests
import allure
import helpers
from constants.urls import Urls

@allure.feature('Тест Регистрация пользователя')
class TestCreateUser:
    @allure.title('Регистрация пользователя с корректными данными')
    @allure.description(
        'Пользователь с корректными данными создается успешно'
    )

    def test_create_user_successful(self, create_user_and_return_data):
        response_data = create_user_and_return_data

        assert response_data['response'].status_code == 200 and response_data['response'].json()['success']

    @allure.title('Тест Повторная регистрация пользователя с тем же данными')
    @allure.description(
        'Регистрация уже зарегистрированного пользователя выдает ошибку и код 403'
    )

    def test_create_user_with_existing_data(self, user_data):
        payload = user_data
        response = requests.post(Urls.CREATE_USER, data=payload)

        assert response.status_code == 403 and response.text == '{"success":false,"message":"User already exists"}'

    @allure.title('Тест Регистрация пользователя без обязательного поля')
    @allure.description(
        'Регистрация пользователя без одного из обязательных полей выдает ошибку и код 403'
    )

    @pytest.mark.parametrize('field', ['email', 'password', 'name'])
    def test_create_user_no_required_field_error(self, field):
        payload = helpers.create_user_data()
        del payload[field]
        response = requests.post(Urls.CREATE_USER, data=payload)

        assert response.status_code == 403
        assert response.text == '{"success":false,"message":"Email, password and name are required fields"}'

