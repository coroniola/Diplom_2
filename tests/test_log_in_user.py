import allure
import requests
from constants.urls import Urls


class TestLoginUser:
    @allure.title('Тест Авторизация существующего пользователя')
    @allure.description('Существующий пользователь может успешно авторизоваться')

    def test_successful_user_login(self, user_data):
        payload = user_data
        response = requests.post(Urls.LOGIN_USER, data=payload)

        assert response.status_code == 200 and response.json()['success']

    @allure.title('Тест Авторизация с неверным email и паролем')
    @allure.description('Авторизация с неверным логином или паролем выдает ошибку и код 401')

    def test_failed_user_login_with_invalid_credentials(self, user_data):
        payload = user_data.copy()
        payload["email"] += 'incorrect'
        payload["password"] += str(1)
        response = requests.post(Urls.LOGIN_USER, data=payload)

        assert response.status_code == 401
        assert response.text == '{"success":false,"message":"email or password are incorrect"}'