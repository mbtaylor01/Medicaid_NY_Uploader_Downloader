import driver
from selenium.webdriver.common.by import By
from settings import SETTINGS as S


def login(chrome_driver):
    """Logs in."""
    #  go to page
    chrome_driver.get(S['login_url'])

    #  find username box, select it, put in username
    username_id = "[id$='_ContentPlaceHolder1_LoginExchange_UserName']"
    username_box = driver.visible_element(chrome_driver, By.CSS_SELECTOR, username_id)
    username_box.send_keys(S["username"])

    #  find password box, select it, put in password
    password_id = "[id$='_ContentPlaceHolder1_LoginExchange_Password']"
    password_box = driver.visible_element(chrome_driver, By.CSS_SELECTOR, password_id)
    password_box.send_keys(S["password"])

    #  find Agree checkbox and click it
    checkbox_id = "[id$='_ContentPlaceHolder1_LoginExchange_chkbxAgree']"
    checkbox = driver.clickable_element(chrome_driver, By.CSS_SELECTOR, checkbox_id)
    checkbox.click()

    #  find login button and click it
    login_id = "[id$='_ContentPlaceHolder1_LoginExchange_LoginButton']"
    login_button = driver.clickable_element(chrome_driver, By.CSS_SELECTOR, login_id)
    login_button.click()
