import driver
import download_functions as dfs
from selenium.webdriver.common.by import By
from settings import SETTINGS as S


def download(chrome_driver):
    "Goes through the download process."

    #  find the Inbox button (where files to download are) and click it
    inbox_button_id = "[id$='_ibInbox']"
    inbox_button = driver.clickable_element(chrome_driver, By.CSS_SELECTOR, inbox_button_id)
    inbox_button.click()

    #  reads last_download.txt for the name of the last downloaded file
    last_download = dfs.last_download()