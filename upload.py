import driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from settings import SETTINGS as S


def upload(chrome_driver):
    """Goes through the upload process."""

    #  find the Send A Batch button and click it
    send_button_id = "[id$='_ibSendBatch']"
    send_button = driver.clickable_element(chrome_driver, By.CSS_SELECTOR, send_button_id)
    send_button.click()

    #  find the dropdown box specifying the type of file to upload and select it
    batch_type_dropdown_id = "[id*='_ContentPlaceHolder1_ddlBatchType']"
    batch_type_dropdown = driver.visible_element(chrome_driver, By.CSS_SELECTOR, batch_type_dropdown_id)
    Select(batch_type_dropdown).select_by_value("Professional Claims.x12")

    
