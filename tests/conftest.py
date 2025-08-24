import pytest
import os
import sys
directory = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.dirname(directory))
from selenium import webdriver
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.wait import WebDriverWait
from credentials import *
from locators import *
from urls_const import *


# Фикстура инициализации драйвера Chrome
@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window() # Раскрываем на весь экран
    yield driver 
    driver.quit() # Закрываем браузер ВО ВСЕХ ТЕСТАХ !!!


# Фикстура открытия главной страницы сайта
@pytest.fixture
def open_main_page(driver):
    driver.get(main_page)
    return driver


# Фикстура входа по кнопке «Войти в аккаунт» на главной странице сайта
@pytest.fixture
def open_main_page_login_page(driver): 
    driver.get(login_page)
    
    # Ищем поля на странице Входа и проходим авторизацию
    driver.find_element(*Locators.enter_email_input).send_keys(Credentials.my_email)
    driver.find_element(*Locators.enter_password_input).send_keys(Credentials.my_password)
    driver.find_element(*Locators.enter_login_button).click()
    return driver


# Фикстура открытия страницы регистрации
@pytest.fixture
def open_register_page(driver):
    driver.get(register_page)
    return driver


# Фикстура открытия страницы восстановления пароля
@pytest.fixture
def open_recovery_pass_page(driver):
    driver.get(recovery_pass) 
    return driver
