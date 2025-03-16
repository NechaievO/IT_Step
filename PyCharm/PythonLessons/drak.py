import random
import time

from selenium import webdriver
from selenium.common.exceptions import (
    TimeoutException
)
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

# Опции браузера
options = webdriver.ChromeOptions()
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("--headless")  # Фоновый режим

# Инициализация браузера
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

def get_cart_count():
    """Возвращает количество товаров в корзине."""
    try:
        cart_count_element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, '//span[@class="checkout_items"]'))
        )
        return int(cart_count_element.text.strip()) if cart_count_element.text.strip().isdigit() else 0
    except Exception:
        print("Ошибка: не удалось найти счетчик корзины.")
        return 0


def add_to_cart_test():
    driver.get("https://www.dracek.cz/")

    # Ожидание загрузки страницы и принятия куки
    try:
        cookie_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//a[@class="__cookiesNlink __cookiesSuccess"]'))
        )
        cookie_button.click()
    except TimeoutException:
        print("Куки уже приняты или кнопка не найдена.")

    try:
        categories = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, '//li[@class="mega-drop-down"]'))
        )

        if categories:
            random_category = random.choice(categories)
            random_category.click()
            print("Перешли в случайную категорию.")
        else:
            print("Категории не найдены.")
            driver.quit()
            return

        added_products = 0
        total_product_count = 32  # Количество товаров, которое нужно добавить

        while added_products < total_product_count:
            add_to_cards_buttons = WebDriverWait(driver, 10).until(
                EC.presence_of_all_elements_located((By.XPATH, '//a[@class="btn main-action buyButton"]'))
            )

            for add_to_cart_button in add_to_cards_buttons:
                if added_products >= total_product_count:
                    break

                try:
                    # Прокрутка к кнопке и клик
                    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", add_to_cart_button)
                    driver.execute_script("arguments[0].click();", add_to_cart_button)
                    time.sleep(1)

                    # Закрытие модального окна
                    try:
                        back_button = WebDriverWait(driver, 5).until(
                            EC.element_to_be_clickable(
                                (By.XPATH, '//a[@class="btn modalGreyButton btn-lg dCloseModal"]'))
                        )
                        back_button.click()
                    except Exception:
                        pass

                    added_products += 1
                    print(f"Добавлен товар {added_products}")

                    # Проверка счетчика корзины
                    cart_count = get_cart_count()
                    if cart_count != added_products:
                        print(f" Ошибка: в корзине {cart_count} товаров, но добавлено {added_products}!")

                except Exception as e:
                    print(f"Ошибка при добавлении товара: {e}")
                    continue

            # Нажатие кнопки "Загрузить больше товаров", если нужно
            if added_products < total_product_count:
                try:
                    next_page = WebDriverWait(driver, 10).until(
                        EC.element_to_be_clickable((By.XPATH, '//a[@class="btn j-more-products nextProducts"]'))
                    )
                    next_page.click()
                except Exception:
                    break

        print(f"Тест завершён: добавлено {added_products} товаров в корзину.")

    except Exception as e:
        print(f"Произошла ошибка: {e}")
    finally:
        print("Закрытие браузера...")
        driver.quit()

add_to_cart_test()