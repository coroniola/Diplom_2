import requests
import helpers
import allure
from constants.urls import Urls

class TestChangeUserData:

    @allure.title('Тест Обновление информации о пользователе')
    @allure.description(
        'Тест проверяет успешное обновление данных авторизованного пользователя'
    )
    def test_update_userdata_successful(self, user_data):
        token = user_data['token']
        payload = {
            "email": user_data['email'] + '1',
            "name": user_data['name'] + '1',
            "password": user_data['password'] + '1'
        }
        response = requests.patch(Urls.DELETE_USER, headers={'Authorization': token}, json=payload)
        assert response.status_code == 200 and response.json()['success']

    @allure.title('Тест Обновления информации неавторизованным пользователем невозможно')
    @allure.description(
       'Тест проверяет ошибку при попытке обновления данных неавторизованным пользователем'
    )
    def test_update_userdata_without_authorization(self, ):
        payload = helpers.create_user_data()
        response = requests.patch(Urls.DELETE_USER, data=payload)
        assert response.status_code == 401
        assert response.text == '{"success":false,"message":"You should be authorised"}'