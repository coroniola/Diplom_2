import requests
import allure
from constants.urls import Urls
from constants.ingredients import Ingredients

class TestCreateOrder:

    @allure.title('Тест Создание заказа')
    @allure.description(
        'Успешное создание заказа'
    )

    def test_authenticated_user_create_order_success(self, user_token):

        token = user_token
        payload = Ingredients.INGREDIENTS
        response = requests.post(Urls.ORDER, headers={'Authorization': token}, data=payload)

        assert response.status_code == 200 and response.json()['success']

    @allure.title('Тест Создание заказа с неверными ингридиентами')
    @allure.description(
        'Создание заказа с неверными ингридиентами выдает ошибку и код 500'
    )
    def test_create_order_bad_ingredients_error(self):

        payload = Ingredients.INCORRECT_INGREDIENTS
        response = requests.post(Urls.ORDER, data=payload)

        assert response.status_code == 500 and 'Internal Server Error' in response.text

    @allure.title('Тест Создание заказа без авторизации пользователя')
    @allure.description(
        'Успешное создание заказа без авторизации пользователя'
    )

    def test_create_order_without_authorization(self):

        payload = Ingredients.INGREDIENTS
        response = requests.post(Urls.ORDER, data=payload)

        assert response.status_code == 200 and response.json()['success']

    @allure.title('Тест Создание заказа без ингредиентов')
    @allure.description(
        'Создание заказа без ингридиентов выдает ошибку и код 400'
    )

    def test_create_order_without_ingredients_error(self):

        payload = Ingredients.WITHOUT_INGREDIENTS
        response = requests.post(Urls.ORDER, data=payload)

        assert response.status_code == 400
        assert response.text == '{"success":false,"message":"Ingredient ids must be provided"}'

