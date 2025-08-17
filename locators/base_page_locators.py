from selenium.webdriver.common.by import By

class BasePageLocators:

    LOGO = By.XPATH, "//div[@class='AppHeader_header__logo__2D0X2']"            # Лого
    BUTTON_TO_CONSTRUCTOR = By.XPATH, "//p[contains(text(), 'Конструктор')]"    # Кнопка "Конструктор" в заголовке страницы
    BUTTON_TO_ORDER_FEED = By.XPATH, "//p[contains(text(), 'Лента Заказов')]"   # Кнопка "Лента Заказов" в заголовке страницы
    BUTTON_TO_PERSONAL_ACCOUNT = By.XPATH, "//a[@href='/account']"              # Кнопка "Личный кабинет" в заголовке страницы
    BUTTON_LOGIN_IN_MAIN = (By.XPATH, './/button[text() = "Войти в аккаунт"]')  # Кнопка "Войти в аккаунт" на главной



