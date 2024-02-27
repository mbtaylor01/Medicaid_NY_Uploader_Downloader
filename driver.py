from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from subprocess import CREATE_NO_WINDOW
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from settings import SETTINGS as S


def create_driver():
    """Creates the web driver object."""
    options = webdriver.ChromeOptions()
    chrome_service = Service(S['driver_path'])
    #  stop the chromedriver.exe popup box from appearing
    chrome_service.creation_flags = CREATE_NO_WINDOW  
    if eval(S['browser_is_headless']):
        #  force browser to be a specific size
        options.add_argument("window-size=1920,1080")
        #  allow downloading while headless
        options.add_argument("--headless=new")  
    else:
        #  stop browser from closing
        options.add_experimental_option("detach", True)  

    return webdriver.Chrome(service=chrome_service, options=options)


def visible_element(driver, by_type, id_type):
    """Waits until the element is visible, then returns it. An exception is raised if there is more than one match."""
    element = WebDriverWait(driver, S["link_timeout_seconds"]).until(
        expected_conditions.visibility_of_element_located((by_type, id_type)))

    if len(driver.find_elements(by_type, id_type)) > 1:
        raise Exception(f"Cannot proceed.  More than one matching visible element found for: {id_type}")
    else:
        return element


def clickable_element(driver, by_type, id_type):
    """Waits until the element is clickable, then returns it. An exception is raised if there is more than one match."""
    element = WebDriverWait(driver, S["link_timeout_seconds"]).until(
        expected_conditions.element_to_be_clickable((by_type, id_type)))

    if len(driver.find_elements(by_type, id_type)) > 1:
        raise Exception(f"Cannot proceed.  More than one matching clickable element found for: {id_type}")
    else:
        return element


