import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators.base_page_locators import BasePageLocators
from locators.constructor_page_locators import ConstructorPageLocators
from locators.order_feed_page_locators import OrderFeedPageLocators
from seletools.actions import drag_and_drop

# класс содержит базовые методы
class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    @allure.step('Открыть страницу')
    def open_page(self, url):
        self.driver.get(url)
        self.wait.until(expected_conditions.url_contains(url))
        self.wait.until(lambda d: d.execute_script("return document.readyState") == "complete")

    @allure.step('Поиск элемента')
    def find_element(self, locator):
        return self.wait.until(expected_conditions.presence_of_element_located(locator))

    @allure.step('Ожидание видимости элемента')
    def wait_for_visible_element(self, locator):
        return self.wait.until(expected_conditions.visibility_of_element_located(locator))

    @allure.step('Ожидание кликабельности элемента')
    def wait_for_clickable_element(self, locator):
        return self.wait.until(expected_conditions.element_to_be_clickable(locator))


    @allure.step('Прокрутить до элемента')
    def scroll_to_element(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        self.wait.until(expected_conditions.element_to_be_clickable(element))
        return element

    @allure.step('Кликнуть элемент')
    def click_to_element_by_script(self, locator):
        element = self.wait_for_visible_element(locator)
        self.driver.execute_script("arguments[0].click();", element)

    @allure.step('Скролл к элементу и кликаем по нему через JS: {locator}')
    def scroll_and_click(self, locator):
        self.wait.until(expected_conditions.presence_of_element_located(locator))
        self.wait.until(expected_conditions.element_to_be_clickable(locator))
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        self.driver.execute_script("arguments[0].click();", element)

    def find_and_focus_by_script(self, element):
        self.wait.until(expected_conditions.presence_of_element_located(element))
        self.driver.execute_script("arguments[0].scrollIntoView();", self.driver.find_element(*element))
        self.wait.until(expected_conditions.element_to_be_clickable(element))

    def get_element(self, element: tuple):
        self.find_and_focus_by_script(element=element)
        return self.driver.find_element(*element)

    @allure.step('Получаем текст из элемента')
    def get_text_from_element(self, locator):
        return self.find_element(locator).text


    @allure.step('Очистить поле и вставить текст')
    def set_text_in_element(self, locator, text):
        element = self.wait_for_clickable_element(locator)
        element.clear()
        element.send_keys(text)

    @allure.step("Обновить страницу и дождаться её полной загрузки")
    def refresh_page_and_wait(self, locator):
        self.driver.refresh()
        self.wait.until(expected_conditions.presence_of_element_located(locator))


    @allure.step('Проверка URL')
    def check_to_url(self):
        return self.driver.current_url

    @allure.step('Перетащить элемент drag-and-drop')
    def drag_and_drop_element(self, locator_from, locator_to):
        source = self.wait_for_visible_element(locator_from)
        target = self.wait_for_visible_element(locator_to)
        with allure.step(f'Перенести из {source} в {target}'):
            drag_and_drop(self.driver, source, target)

    @allure.step('Нажать кнопку "Лента Заказов" в хедере и дождаться загрузки страницы')
    def click_button_feed_of_orders_in_header(self):
        self.scroll_and_click(BasePageLocators.BUTTON_TO_ORDER_FEED)
        self.find_element(OrderFeedPageLocators.HEADER_FEED_OF_ORDERS)

    @allure.step('Ожидание загрузки страницы "Конструктор"')
    def wait_for_constructor_page(self):
        self.find_element(ConstructorPageLocators.TITLE_ASSEMBLE_THE_BURGER)

    @allure.step("Ожидать, пока номер заказа обновится с 9999 на актуальный")
    def wait_for_real_order_number(self, locator):
        self.wait.until(
            lambda driver: (
                    (text := self.find_element(locator).text.replace(" ", "").strip()).isdigit()
                    and text != "9999"
            ),
            message="Номер заказа не обновился с 9999 на реальный"
        )
