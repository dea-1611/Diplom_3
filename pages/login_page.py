import allure
from pages.base_page import BasePage
from urls import *
from locators.personal_account_page_locators import *



class LoginPage(BasePage):

    @allure.step('Открыть страницу авторизации')
    def open_login_page(self):
        self.open_page(Urls.URL_LOGIN_PAGE)

    @allure.step('Заполнить поле "email" на странице авторизации')
    def fill_email_field(self, email):
        self.click_to_element_by_script(PersonalAccountPageLocators.FIELDS_EMAIL)
        self.set_text_in_element(locator=PersonalAccountPageLocators.FIELDS_EMAIL, text=email)

    @allure.step('Заполнить поле "Пароль" на странице авторизации')
    def fill_password_field(self, password):
        self.click_to_element_by_script(PersonalAccountPageLocators.FIELDS_PASSWORD)
        self.set_text_in_element(locator=PersonalAccountPageLocators.FIELDS_PASSWORD, text=password)

    @allure.step('Кликнуть кнопку "Войти" на странице авторизации')
    def click_login_button(self):
        self.click_to_element_by_script(PersonalAccountPageLocators.BUTTON_LOGIN)

    @allure.step('Заполнить поле "email", "Пароль" и кликнуть кнопку "Войти" на странице авторизации')
    def fill_authorize_form_and_click_enter(self, email, password):
        self.fill_email_field(email)
        self.fill_password_field(password)
        self.click_login_button()
        self.wait_for_constructor_page()
