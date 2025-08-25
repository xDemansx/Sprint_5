import pytest
import os
import sys
directory = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.dirname(directory))
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from credentials import *
from locators import *
from urls_const import *


# Тесты страницы "Регистрация"
class TestRegistrationStellarburgers:


    # Тест - OP - Успешная регистрация
    def test_registration_positive(self, open_register_page):
        driver = open_register_page # Открытие страницы регистрации
        
        WebDriverWait(driver, 12).until(EC.visibility_of_element_located(Locators.registration_button)) # Кнопка "Зарегистрироваться"
        driver.find_element(*Locators.registration_name_input).send_keys(Credentials.my_name) # Имя (постоянное)
        driver.find_element(*Locators.registration_email_input).send_keys(Credentials.email()) # Почта (генерируется)
        driver.find_element(*Locators.registration_password_input).send_keys(Credentials.password()) # Пароль (генерируется)
        driver.find_element(*Locators.registration_button).click() # Жмем кнопку "Регистрация"
        
        WebDriverWait(driver, 12).until(EC.visibility_of_element_located(Locators.enter_login_button)) # Ждем кнопку "Войти"
        
        assert driver.current_url == login_page # Сравниваем наш url с f'{main_page}login'
        # Тест проходит PASSED 


    # Тест - OP - Ошибка для некорректного пароля
    def test_registration_negative_password (self, open_register_page):
        driver = open_register_page
        
        WebDriverWait(driver, 12).until(EC.visibility_of_element_located(Locators.registration_button)) # Кнопка "Зарегистрироваться"
        driver.find_element(*Locators.registration_name_input).send_keys(Credentials.my_name) # Имя (постоянное)
        driver.find_element(*Locators.registration_email_input).send_keys(Credentials.email()) # Почта (генерируется)
        driver.find_element(*Locators.registration_password_input).send_keys(Credentials.negative_password) # Пароль (некорректный)
        driver.find_element(*Locators.registration_button).click() # Жмем кнопку "Регистрация"
        
        assert WebDriverWait(driver, 12).until(EC.visibility_of_element_located(Locators.registration_error_password)) # Ждем надпись об ошибке "Некорректный пароль"
        # Тест проходит PASSED 
        