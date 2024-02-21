import driver
import upload_functions as ufs
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from os import remove
from emails import send_email
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

    #  get a list of the files to upload (os.scandir objects)
    files_to_upload = ufs.files_to_upload(S["upload_location"])
    
    for file in files_to_upload:
        #  find the input box, which doesn't seem to be "visible" or "clickable" to the chromedriver
        #  then, send the input box the file's path
        file_input_id = "[id$='_ContentPlaceHolder1_SendFilefile0']"
        file_input = chrome_driver.find_element(By.CSS_SELECTOR, file_input_id)
        file_input.send_keys(file.path)

        #  find the upload button and click it
        upload_button_id = "[id$='_ContentPlaceHolder1_ibSendBatchSubmit']"
        upload_button = driver.clickable_element(chrome_driver, By.CSS_SELECTOR, upload_button_id)
        upload_button.click()

        #  find the span element that contains the upload confirmation message
        confirmation_element_id = "[id$='_ContentPlaceHolder1_lblErrorMessage']"
        confirmation_element = driver.visible_element(chrome_driver, By.CSS_SELECTOR, confirmation_element_id)

        #  if the file is confirmed to be uploaded, delete the file
        if ufs.file_uploaded(confirmation_element):
            remove(file.path)
        else:
            send_email(S["upload_fail_subject"], S["upload_fail_message"])

        #  identify the "<<Back" button that goes back to the upload page and click it
        back_button_id = "[id$='_ContentPlaceHolder1_lbBack']"
        back_button = driver.clickable_element(chrome_driver, By.CSS_SELECTOR, back_button_id)
        back_button.click()
