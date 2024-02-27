import driver
import login
import upload
import download
from emails import send_email
from traceback import format_exc
from time import sleep
from settings import SETTINGS as S


def main():
    try:
        #  create driver
        chrome_driver = driver.create_driver()

        #  log in to the website
        login.login(chrome_driver)

        #  upload files
        upload.upload(chrome_driver)

        #  wait so site has a chance to retrieve the download files
        sleep(30)

        #  download files
        download.download(chrome_driver)

        #  quit driver
        if eval(S['browser_is_headless']):
            chrome_driver.quit()

    except Exception as exception:
        send_email(S["main_fail_subject"], f"{exception}\r\r{format_exc()}")

        chrome_driver.quit()


main()


