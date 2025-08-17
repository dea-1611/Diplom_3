from pages.base_page import BasePage
from locators.order_feed_page_locators import OrderFeedPageLocators
from helpers import *
import allure


class OrderFeedPage(BasePage):

    @allure.step('Получить значение счётчика за всё время')
    def get_counter_value_increases_completed_total(self):
        text = self.get_text_from_element(OrderFeedPageLocators.COUNTER_TOTAL_ORDERS_FOR_ALL_TIME)
        return int(text.replace(" ", ""))  # Удаляем пробелы и преобразуем в число

    @allure.step('Получить значение счётчика за сегодня')
    def get_counter_value_increases_completed_total_today(self):
        text = self.get_text_from_element(OrderFeedPageLocators.COUNTER_TOTAL_ORDERS_FOR_TODAY)
        return int(text.replace(" ", ""))

    @allure.step("Обновить страницу ленты заказов и дождаться загрузки")
    def refresh_feed_of_orders_page_and_wait(self):
        self.refresh_page_and_wait(OrderFeedPageLocators.HEADER_FEED_OF_ORDERS)

    @allure.step("Проверяем наличие номера заказа в разделе 'В работе'")
    def check_order_number_in_progress_section_inside_order_feed(self, order_identifier):
        # Нормализуем номер заказа (удаляем ведущие нули)
        normalized_identifier = order_identifier.lstrip('0')

        # Ждем появления заказа с нормализованным номером
        self.wait.until(
            lambda driver: any(
                normalized_identifier in order.text.lstrip('0')
                for order in driver.find_elements(*OrderFeedPageLocators.ORDERS_IN_WORK)
            ),
            message=f"Заказ {order_identifier} не появился в разделе 'В работе'"
        )

        # Проверяем наличие заказа
        orders = self.driver.find_elements(*OrderFeedPageLocators.ORDERS_IN_WORK)
        order_numbers = [order.text.lstrip('0') for order in orders]
        assert normalized_identifier in order_numbers, (
            f"Заказ {normalized_identifier} не найден в разделе 'В работе'. Найдены: {order_numbers}"
        )