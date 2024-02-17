import driver
from selenium.webdriver.common.by import By
from settings import SETTINGS as S


def upload(chrome_driver):
    """Goes through the upload process."""

    #  find the Send A Batch button and click it
    send_button_id = "[id$='_ibSendBatch']"
    send_button = driver.clickable_element(chrome_driver, By.CSS_SELECTOR, send_button_id)
    send_button.click()

    
