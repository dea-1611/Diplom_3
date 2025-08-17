from selenium.webdriver.common.by import By



class PersonalAccountPageLocators:

    # Основные элементы:
    LOGIN_TITLE = By.XPATH, '//h2[text()="Вход"]'                                     # заголовок страницы "Вход"
    FIELDS_EMAIL = By.XPATH, '//label[text()="Email"]/following-sibling::input'       # поле Email
    FIELDS_PASSWORD = By.XPATH, '//input[@name = "Пароль"]'                           # поле "Пароль"

    BUTTON_LOGIN  = By.XPATH, '//button[text()="Войти"]'                              # кнопка "Войти"
    REGISTER_BUTTON_LOGIN = \
        (By.XPATH, '//a[text() = "Зарегистрироваться"]')                        # ссылка "Зарегистрироваться" в окне авторизации
    FLAG_OF_INCORRECT_PASSWORD = (By.XPATH,
                                  '//p[text() = "Некорректный пароль"]')        # сообщение об ошибке: пароль не прошел валидацию

    BUTTON_SUBMIT = (By.XPATH, '//button[text() = "Зарегистрироваться"]')              # кнопка "Зарегистрироваться"

    BUTTON_EXIT_PERSONAL_ACCOUNT_PAGE_LOCATOR = By.XPATH, ".//button[text()='Выход']"  # кнопка "Выход"

    FIELDS_NAME = (By.XPATH, '//label[text()="Имя"]/following-sibling::input')         # поле "Имя"

