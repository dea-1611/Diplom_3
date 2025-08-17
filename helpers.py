import string
import requests
import allure
import random
from urls import  Endpoints



class TestTools:

    @staticmethod
    def check_ui_test_result(expected_value, actual_value):
        assert expected_value == actual_value, (
            f'\nОжидаемое значение:\n"{expected_value}"\nФактическое значение:\n"{actual_value}"'
        )

class Generators:

    # метод генерирует случайную последовательность из строчных букв латинского алфавита
    @staticmethod
    @allure.step('Генерация случайной последовательности из строчных букв латинского алфавита')
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for _ in range(length))
        return random_string

    # метод генерирует случайную последовательность цифр в формате строки
    @staticmethod
    @allure.step('Генерация случайной последовательности цифр в формате строки')
    def generate_random_numbers_as_string(length):
        numbers = '0123456789'
        random_numbers = ''.join(random.choice(numbers) for _ in range(length))
        return random_numbers

    @staticmethod
    @allure.step('Генерация email')
    def generate_random_email():
        login_name = ''.join(random.choices(string.ascii_lowercase + string.digits, k=random.randint(3, 10)))
        email_name = ''.join(random.choices(string.ascii_lowercase, k=random.randint(2, 6)))
        email_domain = ''.join(random.choices(string.ascii_lowercase, k=2))
        return f"{login_name}@{email_name}.{email_domain}"


    # статический метод генерирует список из валидных случайных: почты, пароля и имени
    @staticmethod
    @allure.step('Генерация пользователя')
    def generate_payload():
        email = (Generators.generate_random_email())
        password = Generators.generate_random_string(6) + Generators.generate_random_numbers_as_string(2)
        name = Generators.generate_random_string(5)
        payload = {
            "email": email,
            "password": password,
            "name": name
        }
        return payload

class User:

    # метод регистрирует нового пользователя
    @staticmethod
    @allure.step('Регистрация пользователя')
    def register_user(user):
        response = requests.post(url=Endpoints.CREATE_USER, json=user)
        return response
