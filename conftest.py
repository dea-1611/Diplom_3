import pytest
import requests
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from helpers import Generators,User
import allure
from urls import Endpoints

@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    driver = None
    try:
        if request.param == "chrome":
            driver = webdriver.Chrome()
        elif request.param == "firefox":
            driver = webdriver.Firefox()
        yield driver
    except WebDriverException as e:
        pytest.fail(f"Не удалось запустить браузер {request.param}. Ошибка: {e}")
    finally:
        if driver is not None:
            driver.quit()


@pytest.fixture(scope='function')
def random_user():
    payload = Generators.generate_payload()
    with allure.step("Создание пользователя через API"):
        response = User.register_user(payload)
        access_token = response.json().get("accessToken")

    yield payload["email"], payload["password"]

    with allure.step("Удаление пользователя через API"):
        if access_token:
            headers = {"Authorization": f"Bearer {access_token}"}
            requests.delete(Endpoints.DELETE_USER, headers=headers)
