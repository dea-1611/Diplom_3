from selenium.webdriver.common.by import By

class ConstructorPageLocators:

    BUNS_BLOCK = By.XPATH, '//span[text()="Булки"]/parent::div'                  # Заголовок раздела "Булки" в меню конструктора
    SAUCES_BLOCK = By.XPATH, '//span[text()="Соусы"]/parent::div'                # Заголовок раздела "Соусы" в меню конструктора
    FILLINGS_BLOCK = By.XPATH, '//span[text()="Начинки"]/parent::div'            # Заголовок раздела "Начинки" в меню конструктора
    TITLE_ASSEMBLE_THE_BURGER = By.XPATH, ".//h1"                                # Надпись, "Соберите бургер"

    # Корзина в виде списка ингредиентов
    BASKET_OF_BURGER_CONSTRUCTOR = By.XPATH, "//ul[@class='BurgerConstructor_basket__list__l9dp_']"

    # Флюоресцентная булка R2-D3 в Корзине
    INGREDIENT_R2_D3_BUN_IN_BASKET_CONSTRUCTOR = By.XPATH, '//span[text()="Флюоресцентная булка R2-D3 (верх)"]'

    BUTTON_PLACE_AN_ORDER = By.XPATH, ".//button[text()='Оформить заказ']"                # кнопка "Оформить заказ"
    INGREDIENT_R2_D3_BUN_LOCATOR = By.XPATH, './/*[text()="Флюоресцентная булка R2-D3"]'  #  Флюоресцентная булка R2-D3
    INGREDIENT_COUNTER_R2_D3_BUN = By.XPATH, './/*[@class="counter_counter__num__3nue1"]' # счетчик ингредиента

# Элементы отображаемые в модальном окне ингредиента

    PROPERTIES_OPEN_MODAL_WINDOW = \
        By.CSS_SELECTOR, "section.Modal_modal_opened__3ISw4"

    MODAL_WINDOW_CLOSED_CONSTRUCTOR = By.CSS_SELECTOR, "section.Modal_modal__P3_V5"

    INGREDIENT_DETAILS_MODAL_WINDOW = \
        (By.XPATH, "//h2[contains(@class, 'Modal_modal__title') and text()='Детали ингредиента']")

    # "крестик" модального окна
    BUTTON_CLOSE_MODAL_WINDOW = \
        By.XPATH, ".//button[@class='Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK']"

    # в модальном окне название булки Флюоресцентная булка R2-D3
    INGREDIENT_R2_D3_BUN_NAME_MODAL_WINDOW = By.XPATH, "//p[@class='text text_type_main-medium mb-8']"

    # в модальном окне текст идентификатор заказа
    TEXT_INDICATOR_ORDER_OF_ORDER_MODAL_WINDOW = By.XPATH, "//p[contains(text(), 'идентификатор заказа')]"

    # в модальном окне номер заказа
    NUMBER_OF_ORDER_MODAL_WINDOW = (By.XPATH, "//h2[contains(@class, 'text text_type_digits-large mb-8')]")


