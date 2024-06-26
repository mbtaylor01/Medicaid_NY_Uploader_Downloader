import driver
import download_functions as dfs
from selenium.webdriver.common.by import By
from time import sleep
from emails import send_email
from settings import SETTINGS as S


def download(chrome_driver):
    "Goes through the download process."

    #  find the Inbox button (where files to download are) and click it
    inbox_button_id = "[id$='_ibInbox']"
    inbox_button = driver.clickable_element(chrome_driver, By.CSS_SELECTOR, inbox_button_id)
    inbox_button.click()

    #  reads last_download.txt for the name of the last downloaded file
    last_download = dfs.last_download()

    files_found_to_download = []

    #  find each link in the file list from top to bottom (100 is arbitrary number)
    for i in range(100):
        link_container_id = f"[id$='_ContentPlaceHolder1_rgdProduction_ctl00__{i}']"
        link_container = driver.visible_element(chrome_driver, By.CSS_SELECTOR, link_container_id)
        link = link_container.find_element(By.TAG_NAME, "a")

        #  if the file doesn't match the last downloaded file, record the name and click the link
        #  if it does match, you've reached the end of new files to download
        if link.text != last_download:
            files_found_to_download.append(link.text)
            link.click()
        else:
            break

    if len(files_found_to_download) > 0:
        #  write the name of the downloaded file that was highest in the list to last_download.txt
        dfs.record_last_download(files_found_to_download)

        #  wait for files to finish downloading
        sleep(5)

        #  move the downloaded files to the specified destination directory
        dfs.move_files(
            files=files_found_to_download,
            frm=S["browser_downloads_location"],
            to=S["final_downloads_location"]
        )

        #  wait for files to finish moving
        sleep(5)

        #  if the files don't exist in the specified directory, send a warning email 
        if not dfs.files_exist(
                    files=files_found_to_download,
                    directory=S["final_downloads_location"]
                ):
            send_email(S["download_fail_subject"], S["download_fail_message"])