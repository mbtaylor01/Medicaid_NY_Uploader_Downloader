from settings import SETTINGS as S


def login_failed(chrome_driver):
    """If the current page is the login page, the login has failed."""
    return chrome_driver.current_url == S["login_url"]