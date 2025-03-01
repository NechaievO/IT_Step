import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from test_folder.data import Full_Name, URL, Email_name, Current_Address, Permanent_Address

options = webdriver.ChromeOptions()
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("useAutomationExtension", False)
# options.add_argument("--start-maximized")

driver = webdriver.Chrome(options=options)

# driver.get('https://demoqa.com/text-box')
driver.get(f'{URL}/text-box')
time.sleep(3)


def fillForm():
    try:
        title = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//h1[text()='Text Box']"))
        )

        print(f'Заголовок {title.text} найден.')

        driver.find_element(By.ID, "userName").send_keys(Full_Name)
        driver.find_element(By.ID, "userEmail").send_keys(Email_name)

        driver.find_element(By.ID, "currentAddress").send_keys(Current_Address)
        driver.find_element(By.ID, "permanentAddress").send_keys(Permanent_Address)

        driver.find_element(By.ID, "submit").click()
        print("Форма отправлена!")

        output_block = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "border"))
        )
        print("Подтверждение появилось!")

        name_text = driver.find_element(By.ID, "name").text.replace("Name:", "").strip()
        email_text = driver.find_element(By.ID, "email").text.replace("Email:", "").strip()
        current_address_text = driver.find_element(By.ID, "currentAddress").get_attribute("value")
        permanent_address_text = driver.find_element(By.ID, "permanentAddress").get_attribute("value")

        assert name_text == Full_Name, f"Ошибка: ожидалось {Full_Name}, а получено {name_text}"
        assert email_text == Email_name, f"Ошибка: ожидалось {Email_name}, а получено {email_text}"
        assert current_address_text == Current_Address, f"Ошибка: ожидалось {Current_Address}, а получено {current_address_text}"
        assert permanent_address_text == Permanent_Address, f"Ошибка: ожидалось {Permanent_Address}, а получено {permanent_address_text}"

        print("Тест успешно пройден: все данные совпадают!")

    except Exception as e:
        print(f"Ошибка: {e}")

    finally:
        driver.quit()


fillForm()