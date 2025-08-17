import allure
from urls import *
from pages.login_page import LoginPage
from pages.constructor_page import ConstructorPage
from pages.order_feed_page import OrderFeedPage



class TestOrderFeed:

    @allure.title('Проверка увеличения счётчика «Выполнено за всё время» при создании нового заказа')
    @allure.description('Открываем страницу "Авторизации" сервиса «Stellar Burgers», '
                        'входим в сервис под созданным пользователем, переходим в окно "Лента заказов" '
                        'и запоминаем текущее значение счетчика заказов, сделанных за ВСЁ ВРЕМЯ, '
                        'переходим в окно конструктора и создаем заказ, снова переходим в окно "Лента заказов" '
                        'и запоминаем новое значение счетчика заказов, сделанных за ВСЁ ВРЕМЯ, '
                        'сравниваем старое и новое значение счетчиков заказов')
    @allure.story('Проверка раздела «Лента заказов»')
    @allure.link(URL_MAIN_PAGE, name='Учебный сервис «Stellar Burgers»')
    def test_increases_completed_total_counter_when_new_order_created(self, driver, random_user):
        email, password = random_user
        login_page = LoginPage(driver)
        login_page.open_login_page()
        login_page.fill_authorize_form_and_click_enter(email, password)
        login_page.click_button_feed_of_orders_in_header()
        order_feed_page = OrderFeedPage(driver)
        counter_before = order_feed_page.get_counter_value_increases_completed_total()
        constructor_page = ConstructorPage(driver)
        constructor_page.click_button_constructor_in_header()
        constructor_page.drag_and_drop_and_verify_r2_d3()
        constructor_page.click_create_order_button()
        constructor_page.click_button_close_modal_window()
        constructor_page.click_button_feed_of_orders_in_header()
        order_feed_page.refresh_feed_of_orders_page_and_wait()
        counter_after = order_feed_page.get_counter_value_increases_completed_total()
        with allure.step('Сравнить значения счётчиков ДО и ПОСЛЕ оформления заказа, счётчик ПОСЛЕ должен увеличиться'):
            assert counter_before < counter_after, f"Счётчик не увеличился после создания нового заказа"


    @allure.title('Проверка увеличения счётчика «Выполнено за сегодня» при создании нового заказа')
    @allure.description('Открываем страницу "Авторизации" сервиса «Stellar Burgers», '
                        'входим в сервис под созданным пользователем, переходим в окно "Лента заказов" '
                        'и запоминаем текущее значение счетчика заказов, сделанных за СЕГОДНЯ, '
                        'переходим в окно конструктора и создаем заказ, снова переходим в окно "Лента заказов" '
                        'и запоминаем новое значение счетчика заказов, сделанных за СЕГОДНЯ, '
                        'сравниваем старое и новое значение счетчиков заказов')
    @allure.story('Проверка раздела «Лента заказов»')
    @allure.link(URL_MAIN_PAGE, name='Учебный сервис «Stellar Burgers»')
    def test_increases_completed_total_today_counter_when_new_order_created(self, driver, random_user):
        email, password = random_user
        login_page = LoginPage(driver)
        login_page.open_login_page()
        login_page.fill_authorize_form_and_click_enter(email, password)
        login_page.click_button_feed_of_orders_in_header()
        order_feed_page = OrderFeedPage(driver)
        counter_before = order_feed_page.get_counter_value_increases_completed_total_today()
        constructor_page = ConstructorPage(driver)
        constructor_page.click_button_constructor_in_header()
        constructor_page.drag_and_drop_and_verify_r2_d3()
        constructor_page.click_create_order_button()
        constructor_page.click_button_close_modal_window()
        constructor_page.click_button_feed_of_orders_in_header()
        order_feed_page.refresh_feed_of_orders_page_and_wait()
        counter_after = order_feed_page.get_counter_value_increases_completed_total_today()
        with allure.step('Сравнить значения счётчиков ДО и ПОСЛЕ оформления заказа, счётчик ПОСЛЕ должен увеличиться'):
            assert counter_before < counter_after, f"Счётчик не увеличился после создания нового заказа"


    @allure.title('Проверка появления номер заказа в разделе «В работе» после его оформления')
    @allure.description('Открываем страницу "Авторизации" сервиса «Stellar Burgers», '
                        'входим в сервис под созданным пользователем,  '
                        'переходим в окно конструктора и создаем заказ и запоминаем номер , '
                        'снова переходим в окно "Лента заказов" '
                        'и проверяем появления этого номер заказа в разделе «В работе»')
    @allure.story('Проверка раздела «Лента заказов»')
    @allure.link(URL_MAIN_PAGE, name='Учебный сервис «Stellar Burgers»')
    def test_after_placing_order_number_appears_in_progress_section(self, driver, random_user):
        email, password = random_user
        login_page = LoginPage(driver)
        login_page.open_login_page()
        login_page.fill_authorize_form_and_click_enter(email, password)
        constructor_page = ConstructorPage(driver)
        constructor_page.drag_and_drop_and_verify_r2_d3()
        constructor_page.click_create_order_button()
        order_identifier = constructor_page.get_number_of_order()
        constructor_page.click_button_close_modal_window()
        constructor_page.click_button_feed_of_orders_in_header()
        order_feed_page = OrderFeedPage(driver)
        order_feed_page.refresh_feed_of_orders_page_and_wait()
        order_feed_page.check_order_number_in_progress_section_inside_order_feed(order_identifier=order_identifier)


