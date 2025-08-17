from pages.base_page import BasePage
from locators.order_feed_page_locators import OrderFeedPageLocators
from helpers import *
import allure


class OrderFeedPage(BasePage):

    @allure.step('Получить значение счётчика в ленте заказов за ВСЕ ВРЕМЯ')
    def get_counter_value_increases_completed_total(self):
        return self.get_text_from_element(OrderFeedPageLocators.COUNTER_TOTAL_ORDERS_FOR_ALL_TIME)

    @allure.step('Получить значение счётчика в ленте заказов за ВСЕ ВРЕМЯ')
    def get_counter_value_increases_completed_total_today(self):
        return self.get_text_from_element(OrderFeedPageLocators.COUNTER_TOTAL_ORDERS_FOR_TODAY)

    @allure.step("Обновить страницу ленты заказов и дождаться загрузки")
    def refresh_feed_of_orders_page_and_wait(self):
        self.refresh_page_and_wait(OrderFeedPageLocators.HEADER_FEED_OF_ORDERS)

    @allure.step("Проверяем наличие номера сделанного заказа в разделе 'В работе' в 'Ленте заказов'")
    def check_order_number_in_progress_section_inside_order_feed(self, order_identifier):
        TestTools.check_ui_test_result(expected_value=order_identifier, actual_value=self.get_element(OrderFeedPageLocators.ORDERS_IN_WORK).text.lstrip('0'))

