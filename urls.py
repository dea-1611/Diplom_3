URL_MAIN_PAGE = "https://stellarburgers.nomoreparties.site/"


class Urls:

    URL_LOGIN_PAGE = URL_MAIN_PAGE + "login"
    URL_PERSONAL_ACCOUNT_PAGE = URL_MAIN_PAGE + "account/profile"
    URL_ORDERS_HISTORY_PAGE = URL_MAIN_PAGE + "account/order-history"
    URL_FEED_OF_ORDERS_PAGE = URL_MAIN_PAGE + "feed" 


class Endpoints:

    # Request_URL
    CREATE_USER = f"{URL_MAIN_PAGE}/api/auth/register"
    DELETE_USER = f"{URL_MAIN_PAGE}/api/auth/user"
    LOGIN_USER = f"{URL_MAIN_PAGE}/api/auth/login"
    INGREDIENTS_INFO = f"{URL_MAIN_PAGE}api/ingredients"

