import allure
from pages.base_page import BasePage
from urls import *
from locators.constructor_page_locators import ConstructorPageLocators
from locators.base_page_locators import BasePageLocators


class ConstructorPage(BasePage):

    @allure.step('Открыть страницу "Конструктор"')
    def open_constructor_page(self):
        self.open_page(URL_MAIN_PAGE)

    @allure.step('Нажать кнопку "Конструктор" в хедере и дождаться загрузки страницы')
    def click_button_constructor_in_header(self):
        self.scroll_and_click(BasePageLocators.BUTTON_TO_CONSTRUCTOR)
        self.wait_for_constructor_page()

    @allure.step('Ожидание появления окна свойств ингредиент')
    def wait_for_ingredient_window(self):
        self.find_element(ConstructorPageLocators.PROPERTIES_OPEN_MODAL_WINDOW)

    @allure.step('Кликнуть булку "Флюоресцентная булка R2-D3" и дождаться появления окна его свойств')
    def click_button_ingredient_in_constructor(self):
        self.scroll_and_click(ConstructorPageLocators.INGREDIENT_R2_D3_BUN_LOCATOR)
        self.wait_for_ingredient_window()

    @allure.step('Получить название ингредиента в модальном окне: "Флюоресцентная булка R2-D3"')
    def get_name_ingredient_details(self):
        return self.get_text_from_element(ConstructorPageLocators.INGREDIENT_R2_D3_BUN_NAME_MODAL_WINDOW)

    @allure.step('Проверка отображения открытого модального окна')
    def is_displayed_opened_modal_window(self):
        modal_window = self.wait_for_visible_element(ConstructorPageLocators.PROPERTIES_OPEN_MODAL_WINDOW)
        return modal_window.is_displayed()

    @allure.step('Проверка отображения модального окна')
    def is_displayed_closed_modal_window(self):
        return self.find_element(ConstructorPageLocators.MODAL_WINDOW_CLOSED_CONSTRUCTOR).is_displayed()

    @allure.step('Кликнуть на крестик для закрытия модального окна и дождаться закрытия')
    def click_button_close_modal_window(self):
        self.click_to_element_by_script(ConstructorPageLocators.BUTTON_CLOSE_MODAL_WINDOW)
        self.wait_for_constructor_page()

    @allure.step('Проверка отображения "Соберите бургер"')
    def get_title_assemble_the_burger(self):
        return self.get_text_from_element(ConstructorPageLocators.TITLE_ASSEMBLE_THE_BURGER)

    @allure.step('Получить значение счётчика ингредиента')
    def get_ingredient_counter_value(self):
        return self.get_text_from_element(ConstructorPageLocators.INGREDIENT_COUNTER_R2_D3_BUN)

    @allure.step('Перетащить булку "Флюоресцентная булка R2-D3" в корзину и проверить её отображение в корзине')
    def drag_and_drop_and_verify_r2_d3(self):
        self.drag_and_drop_element(ConstructorPageLocators.INGREDIENT_R2_D3_BUN_LOCATOR,
                                   ConstructorPageLocators.BASKET_OF_BURGER_CONSTRUCTOR)
        return self.get_text_from_element(ConstructorPageLocators.INGREDIENT_R2_D3_BUN_IN_BASKET_CONSTRUCTOR)

    @allure.step('Кликнуть кнопку "Оформить заказ" на странице "Конструктор" и '
                 'дождаться видимости номера заказа в открывшемся окне')
    def click_create_order_button(self):
        self.click_to_element_by_script(ConstructorPageLocators.BUTTON_PLACE_AN_ORDER)
        self.wait_for_real_order_number(ConstructorPageLocators.NUMBER_OF_ORDER_MODAL_WINDOW)

    @allure.step('Получить номер заказа')
    def get_number_of_order(self):
        identifier = self.get_element(ConstructorPageLocators.NUMBER_OF_ORDER_MODAL_WINDOW).text
        return identifier

