import time
import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from settings import valid_password, valid_email

@pytest.fixture()
def auth_pets():

    service = ChromeService(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    driver.implicitly_wait(10)

    # Переходим на страницу авторизации
    driver.get('http://petfriends.skillfactory.ru/login')

    driver.maximize_window()

    # Вводим email
    element = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.ID, 'email'))).send_keys(valid_email)

    # Вводим пароль
    element = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.ID, 'pass'))).send_keys(valid_password)

    # Нажимаем на кнопку входа в аккаунт
    element = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[type="submit"]'))).click()
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "Мои питомцы")))
    # Нажимаем на ссылку "Мои питомцы"
    element = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, '//a[contains(text(),"Мои питомцы")]'))).click()
    time.sleep(2)

    yield driver

    driver.quit()

