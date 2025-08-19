from pages.base_page import BasePage
from locators.order_feed_page_locators import OrderFeedPageLocators
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
        normalized_identifier = ''.join(filter(str.isdigit, order_identifier)).lstrip('0')

        def order_in_progress(_):
            found_orders = self.find_elements(OrderFeedPageLocators.ORDERS_IN_WORK)
            for order in found_orders:
                try:
                    order_text = ''.join(filter(str.isdigit, order.text)).lstrip('0')
                    if normalized_identifier == order_text:
                        return True
                except:
                    continue
            return False

        self.wait_until_custom(
            order_in_progress,
            message=f"Заказ {order_identifier} не появился в разделе 'В работе'"
        )

        orders_elements = self.find_elements(OrderFeedPageLocators.ORDERS_IN_WORK)
        order_numbers = []
        for order in orders_elements:
            try:
                order_text = ''.join(filter(str.isdigit, order.text)).lstrip('0')
                order_numbers.append(order_text)
            except:
                continue

        assert normalized_identifier in order_numbers, (
            f"Заказ {normalized_identifier} не найден в разделе 'В работе'. "
            f"Найдены заказы: {order_numbers}"
        )
