# Импортируем нужные модули
from selenium import webdriver
import time
import random
import json
import re
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

def price_sorting():
    try:
        driver.get(url="https://www.datart.cz/")
        time.sleep(3)

        # Принятие куки
        try:
            cookie_button = driver.find_element(By.XPATH, '//*[@id="c-p-bn"]')
            cookie_button.click()
            time.sleep(3)
        except NoSuchElementException:
            print("Куки-попап не найден, продолжаем.")

        # Выбираем случайную категорию
        categories = driver.find_elements(By.XPATH, "//li[@class='main-menu-catalog-category']")
        if categories:
            random_category = random.choice(categories)
            driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", random_category)
            driver.execute_script("arguments[0].focus();", random_category)
            random_category.click()
            time.sleep(5)
            print("Выбрана категория")
        else:
            print("Категории не найдены.")
        #driver.quit()
        #exit()


        # Ждем загрузки подкатегорий
        wait.until(EC.presence_of_element_located((By.ID, "snippet--login-refresh")))
        subcategories = driver.find_elements(By.CLASS_NAME, "category-tree-box.bg-white")

        if subcategories:
            random_subcategory = random.choice(subcategories)
            driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", random_subcategory)
            driver.execute_script("arguments[0].focus();", random_subcategory)
            random_subcategory.click()
            time.sleep(5)
            print("Выбрана подкатегория")
        else:
            print("Подкатегории не найдены.")
            driver.quit()
            exit()

        # Сортировка товаров по цене: от наименьшей к наибольшей
        sorting_button = driver.find_element(By.XPATH, "//a[@data-lb-name='Nejlevnější']")
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", sorting_button)
        driver.execute_script("arguments[0].focus();", sorting_button)
        time.sleep(5)
        wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@data-lb-name='Nejlevnější']"))).click()
        try:
            wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@data-lb-name='Nejlevnější']"))).click()
        except:
            driver.execute_script("arguments[0].click();", sorting_button)
        time.sleep(5)

        # Сбор информации о товарах
        time.sleep(7)
        product_elements = driver.find_elements(By.XPATH, "//div[@class='product']")
        products_data = []

        try:
            close_button = driver.find_element(By.XPATH, "//*[contains(@class, 'popup-close')]")
            close_button.click()
            print("Закрыл всплывающее окно")
            time.sleep(2)
        except NoSuchElementException:
            print("Всплывающего окна нет, продолжаем")


        for product in product_elements:
            try:
                name = product.find_element(By.XPATH, ".//h3[@class='item-title']").text
            except NoSuchElementException:
                name = "Название не найдено"

            try:
                description = product.find_element(By.XPATH, ".//div[@class='item-description']").text
            except NoSuchElementException:
                description = "Описание не найдено"

            try:
                price_text = product.find_element(By.XPATH, ".//div[@class='actual ']").text
                price = float(re.sub(r'[^\d,]', '', price_text).replace(",", "."))
            except NoSuchElementException:
                price = "Цена не найдена"

            products_data.append({"Название": name, "Описание": description, "Цена": price})



        # Сохранение в текстовый файл
        with open("results.txt", "w", encoding="utf-8") as file:
            for product in products_data:
                file.write(f"Название: {product['Название']}\n")
                file.write(f"Описание: {product['Описание']}\n")
                file.write(f"Цена: {product['Цена']} CZK\n")
                file.write("-" * 30 + "\n")

        # Сохранение в JSON
        with open("results.json", "w", encoding="utf-8") as json_file:
            json.dump(products_data, json_file, ensure_ascii=False, indent=4)

        print("Данные сохранены в файлы results.txt и results.json")

    except Exception as ex:
        print(f"Ошибка во время выполнения теста: {ex}")

    finally:
        driver.quit()
        print("Браузер закрыт.")

# Запуск теста
price_sorting()