# Импортируем нужные модули для работы с браузером и веб-элементами
from selenium import webdriver
import time
import random
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re


# Опции браузера
options = webdriver.ChromeOptions()
options.add_argument(
    "--disable-blink-features=AutomationControlled")  # Отключение автоматического определения бот-активности
options.add_argument("--start-maximized")  # Запуск браузера в полноэкранном режиме

# Инициализация браузера
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
wait = WebDriverWait(driver, 10)

def search_datart():
    driver.get(url="https://www.datart.cz/")
    time.sleep(3)

    # Согласие с куки, кликаем на кнопку для подтверждения
    driver.find_element(By.XPATH, '//*[@id="c-p-bn"]').click()
    time.sleep(8)

    try:
        look_field = driver.find_element(By.XPATH,'//input[@type="search"]')
        look_field.send_keys("Iphone")

        look_submit_Button = driver.find_element(By.CLASS_NAME,  "search-widget__input-submit")
        look_submit_Button.click()
        print("Поиск выполнен успешно!")

        time.sleep(3)  # Можно заменить на WebDriverWait при необходимости
        product_containers = driver.find_elements(By.XPATH, "//div[@class='col-md-6 col-xl-4']")
        wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='col-md-6 col-xl-4']")))
        products = [p.find_element(By.XPATH, ".//h3[@class='item-title']").text for p in product_containers]
        matching_products = [p.text for p in products if "Iphone" in p.text.lower()]
        print(f"Найдено товаров с '{products}': {len(matching_products)}")

        # Вывод результата
        if len(matching_products) >= 2:
            print("Тест пройден!")
        else:
            print("Тест провален!")

    except Exception as ex:
        print(ex)

    finally:
        time.sleep(5)  # Ожидание перед закрытием
        driver.quit()
        print("Браузер закрыт.")


# Запуск теста
search_datart()