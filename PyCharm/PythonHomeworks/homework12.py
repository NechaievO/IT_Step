#Задание 1: Написать тест на успешный вход



from selenium.webdriver import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from config_homework import URL, correct_login, correct_password


# Опции браузера
options = webdriver.ChromeOptions()
options.add_argument("--disable-blink-features=AutomationControlled")
# options.add_argument("--start-maximized")

# Инициализация браузера
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
wait = WebDriverWait(driver, 10)


def correct_login_datart():

    try:
        driver.get(URL)

        # Согласие с куки
        coockie_btn = wait.until(EC.element_to_be_clickable((By.ID, "c-p-bn")))
        coockie_btn.click()

        login_btn = wait.until(EC.presence_of_element_located((By.ID, "head-login-sign-up")))
        login_btn.click()


        login_field = wait.until(EC.presence_of_element_located((By.ID, "frm-login")))
        login_field.clear()
        login_field.send_keys(correct_login)

        password_field = wait.until(EC.presence_of_element_located((By.ID, "frm-password")))
        password_field.send_keys(correct_password)

        submit_btn = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "btn.btn-login")))
        submit_btn.click()

        login_user_name = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "login-user-name"))).text

        if   login_user_name == "Oleh N.":
            print("Correct Enter - Test Passed ")

        else:
            print("Incorrect Password - Test Failed")


        time.sleep(8)
    except NoSuchElementException:
        print("Element Not Found")



correct_login_datart()