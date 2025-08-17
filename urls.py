URL_MAIN_PAGE = "https://stellarburgers.nomoreparties.site/"       # раздел "Конструктор"


class Urls:

    URL_LOGIN_PAGE = URL_MAIN_PAGE + "login"                           # раздел "Авторизация"
    URL_PERSONAL_ACCOUNT_PAGE = URL_MAIN_PAGE + "account/profile"      # раздел "Личный кабинет
    URL_ORDERS_HISTORY_PAGE = URL_MAIN_PAGE + "account/order-history"  # раздел "История заказов"
    URL_FEED_OF_ORDERS_PAGE = URL_MAIN_PAGE + "feed"                   # раздел "Лента заказов"


class Endpoints:

    # Request_URL
    CREATE_USER = f"{URL_MAIN_PAGE}/api/auth/register"            # регистрация пользователя
    DELETE_USER = f"{URL_MAIN_PAGE}/api/auth/user"                # удаление пользователя
    LOGIN_USER = f"{URL_MAIN_PAGE}/api/auth/login"                # авторизация пользователя
    INGREDIENTS_INFO = f"{URL_MAIN_PAGE}api/ingredients"          # для получения данных об ингредиентах

