from urls import *
from pages.login_page import LoginPage
from pages.constructor_page import ConstructorPage
from helpers import *
import allure


class TestMainFunctionality:

    @allure.title('Проверка на страницу "Конструктор" по нажатию кнопки «Конструктор» в верхней части страницы')
    @allure.description('Открываем страницу "Авторизации" сервиса «Stellar Burgers», '
                        'затем переходим в окно "Конструктор" через кнопку "Конструктор" в верхней части страницы, '
                        'сравниваем фактический адрес с ожидаемым адресом')
    @allure.story('Проверка основного функционала')
    @allure.link(URL_MAIN_PAGE, name='Учебный сервис «Stellar Burgers»')
    def test_navigate_to_constructor_page(self, driver):
        login_page = LoginPage(driver)
        login_page.open_login_page()
        constructor_page = ConstructorPage(driver)
        constructor_page.click_button_constructor_in_header()
        current_url = login_page.check_to_url()
        with allure.step('Сравнить текущий URL с ожидаемым'):
            TestTools.check_ui_test_result(current_url, URL_MAIN_PAGE)


    @allure.title('Проверка перехода на страницу «Лента заказов» по нажатию кнопки "Лента заказов" в верхней части страницы')
    @allure.description('Открываем главную страницу сервиса «Stellar Burgers», '
                        'затем переходим на страницу «Лента заказов» по нажатию кнопки "Лента заказов" в верхней части страницы, '
                        'сравниваем фактический адрес с ожидаемым адресом')
    @allure.story('Проверка основного функционала')
    @allure.link(URL_MAIN_PAGE, name='Учебный сервис «Stellar Burgers»')
    def test_navigate_to_feed_of_orders_page(self, driver):
        constructor_page = ConstructorPage(driver)
        constructor_page.open_constructor_page()
        constructor_page.click_button_feed_of_orders_in_header()
        current_url = constructor_page.check_to_url()
        with allure.step('Сравнить текущий URL с ожидаемым'):
            TestTools.check_ui_test_result(current_url, Urls.URL_FEED_OF_ORDERS_PAGE)


    @allure.title(
        'Проверка появление всплывающего окна с деталями выбранного ингредиента')
    @allure.description(
        'Открываем главную страницу сервиса «Stellar Burgers», '
        'выбираем и кликаем на ингредиент и ждём появление всплывающего окна с деталями выбранного ингредиента, '
        'проверяем имя выбранного ингредиента в окне его свойств')
    @allure.story('Проверка основного функционала')
    @allure.link(URL_MAIN_PAGE, name='Учебный сервис «Stellar Burgers»')
    def test_window_appearance_with_details_should_display_correct_info(self, driver):
        constructor_page = ConstructorPage(driver)
        constructor_page.open_constructor_page()
        constructor_page.click_button_ingredient_in_constructor()
        ingredient_title = constructor_page.get_name_ingredient_details()
        with allure.step('Проверить открытие окна и соответствие заголовка ожидаемому'):
            assert constructor_page.is_displayed_opened_modal_window(), "Всплывающее окно не открыто"
            expected_title = "Флюоресцентная булка R2-D3"
            TestTools.check_ui_test_result(expected_title, ingredient_title)

    @allure.title('Проверка возможности закрытия всплывающего окна с помощью клика по крестику')
    @allure.description(
        'Открываем главную страницу сервиса «Stellar Burgers», '
        'выбираем и кликаем на ингредиент и ждём появление всплывающего окна с деталями выбранного ингредиента, '
        'кликаем на крести, ждем закрытие окна')
    @allure.story('Проверка основного функционала')
    @allure.link(URL_MAIN_PAGE, name='Учебный сервис «Stellar Burgers»')
    def test_closing_window_clicking_on_cross(self, driver):
        constructor_page = ConstructorPage(driver)
        constructor_page.open_constructor_page()
        constructor_page.click_button_ingredient_in_constructor()
        constructor_page.click_button_close_modal_window()
        expected_title = "Соберите бургер"
        actual_title = constructor_page.get_title_assemble_the_burger()
        with allure.step('Проверить закрытие окна и соответствие заголовка ожидаемому'):
            assert constructor_page.is_displayed_closed_modal_window(), "Окно не закрылось"
            TestTools.check_ui_test_result(expected_title, actual_title)


    @allure.title('Проверка увелечения счетчика ингредиента при добавлении ингредиента в заказ')
    @allure.description(
        'Открываем главную страницу сервиса «Stellar Burgers», '
        'выбираем ингредиент и переносим его в корзину, проверяем увеличения счетчика ингредиента')
    @allure.story('Проверка основного функционала')
    @allure.link(URL_MAIN_PAGE, name='Учебный сервис «Stellar Burgers»')
    def test_increasing_the_ingredient_counter_adding_order(self, driver):
        constructor_page = ConstructorPage(driver)
        constructor_page.open_constructor_page()
        expected_value = constructor_page.get_ingredient_counter_value()
        constructor_page.drag_and_drop_and_verify_r2_d3()
        actual_value = constructor_page.get_ingredient_counter_value()
        with allure.step('Проверка добавления нужного ингредиента в корзину и увеличения счетчика ингредиента'):
            # Проверяем, что значение счётчика увеличилось
            assert actual_value > expected_value, (
                f'\nОжидаемое значение (до добавления):\n"{expected_value}"\n'
                f'Фактическое значение (после добавления):\n"{actual_value}"'
            )


