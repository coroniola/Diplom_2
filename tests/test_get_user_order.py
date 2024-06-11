import requests
import allure
from constants.urls import Urls

class TestGetUserOrder:

    @allure.title('Тест Успешное получение заказа пользователя')
    @allure.description(
        'Пользователь может получить заказы при помощи токена.'
    )
    def test_get_order_successful(self, user_token):

        token = user_token
        response = requests.get(Urls.ORDER, headers={'Authorization': token})

        assert response.status_code == 200 and response.json()['success']

    @allure.title('Тест Невозможно получить заказ пользователя без авторизации')
    @allure.description(
        'При попытке получения заказа пользователя без авторизации выдается ошибка'
    )
    def test_get_order_without_token(self):

        token = None
        response = requests.get(Urls.ORDER, headers={'Authorization': token})

        assert response.status_code == 401 and response.text == '{"success":false,"message":"You should be authorised"}'