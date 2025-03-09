# Импортируем нужные модули
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Опции браузера
options = webdriver.ChromeOptions()
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("--start-maximized")

# Инициализация браузера
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
wait = WebDriverWait(driver, 10)

def search_datart():
    try:
        # Открываем сайт
        driver.get("https://www.datart.cz/")
        wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))

    except Exception:
        print("Ошибка: сайт не загрузился!")
        driver.quit()
        exit()

    time.sleep(3)

    # Принятие куки
    try:
        cookie_button = driver.find_element(By.XPATH, '//*[@id="c-p-bn"]')
        cookie_button.click()
        time.sleep(3)
    except NoSuchElementException:
        print("Куки-попап не найден, продолжаем.")

    try:
        # Поиск строки поиска
        search_field = driver.find_element(By.XPATH, '//input[@type="search"]')
        search_field.send_keys("Iphone")

        # Кнопка поиска
        search_button = driver.find_element(By.CLASS_NAME, "search-widget__input-submit")
        search_button.click()

        print("Поиск выполнен успешно!")

        # Ждем загрузки результатов
        wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='col-md-6 col-xl-4']")))

        # Поиск всех товаров
        product_containers = driver.find_elements(By.XPATH, "//div[@class='col-md-6 col-xl-4']")
        products = [p.find_element(By.XPATH, ".//h3[@class='item-title']").text for p in product_containers]

        # Фильтрация товаров по ключевому слову (независимо от регистра)
        matching_products = [p for p in products if "iphone" in p.lower()]
        print(f"Найдено товаров с 'iphone': {len(matching_products)}")

        # Запись в файл
        with open("results.txt", "w", encoding="utf-8") as file:
            file.write(f"Найдено товаров с 'iphone': {len(matching_products)}\n")

        # Проверка условия теста
        if len(matching_products) >= 2:
            print("Тест пройден!")
        else:
            print("Тест провален!")

    except Exception as ex:
        print(f"Ошибка во время теста: {ex}")

    finally:
        time.sleep(5)
        driver.quit()
        print("Браузер закрыт.")

# Запуск теста
search_datart()