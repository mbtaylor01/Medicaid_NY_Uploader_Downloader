import driver
import login
import upload
import download
from settings import SETTINGS as S


def main():
    #  create driver
    chrome_driver = driver.create_driver()

    login.login(chrome_driver)

    # upload files
    upload.upload(chrome_driver)

    #  download files
    download.download(chrome_driver)

    # quit driver
    if eval(S['browser_is_headless']):
        chrome_driver.quit()

main()
