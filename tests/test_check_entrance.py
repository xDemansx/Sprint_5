from typing import Any
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


# Тесты на вход в аккаунт разными способами
class TestAccountEntrance:


    # Тест - ОР - вход по кнопке «Войти в аккаунт» на главной странице сайта
    def test_main_enter_button_entrance(self, open_main_page):
        driver = open_main_page # Вызов фикстуры открытия главной страницы сайта
        
        WebDriverWait(driver, 12).until(EC.visibility_of_element_located(Locators.main_enter_button)) # Ждем кнопку "Войти в аккаунт" на главной странице
        driver.find_element(*Locators.main_enter_button).click() # Жмем кнопку "Войти в аккаунт"
        
        WebDriverWait(driver, 12).until(EC.visibility_of_element_located(Locators.enter_login_button)) # Ждем кнопку "Войти" на странице входа
        driver.find_element(*Locators.enter_email_input).send_keys(Credentials.my_email) # Вносим Email (постоянный)
        driver.find_element(*Locators.enter_password_input).send_keys(Credentials.my_password) # Вносим Password (постоянный)
        driver.find_element(*Locators.enter_login_button).click() # Жмем кнопку "Войти"
        
        assert WebDriverWait(driver, 12).until(EC.visibility_of_element_located(Locators.main_order_button)) # Ждем кнопку "Оформить заказ" на главной странице
        # Тест проходит PASSED 


    # Тест - ОР - вход через кнопку «Личный кабинет» на главной странице сайта
    def test_main_account_button_entrance(self, open_main_page):
        driver = open_main_page # Вызов фикстуры открытия главной страницы сайта
        
        WebDriverWait(driver, 12).until(EC.visibility_of_element_located(Locators.main_account_button)) # Ждем кнопку "Личный кабинет" на главной странице
        driver.find_element(*Locators.main_account_button).click() # Жмем кнопку "Личный кабинет"
        
        WebDriverWait(driver, 12).until(EC.visibility_of_element_located(Locators.enter_login_button)) # Ждем кнопку "Войти" на странице входа
        driver.find_element(*Locators.enter_email_input).send_keys(Credentials.my_email) # Вносим Email (постоянный)
        driver.find_element(*Locators.enter_password_input).send_keys(Credentials.my_password) # Вносим Password (постоянный)
        driver.find_element(*Locators.enter_login_button).click() # Жмем кнопку "Войти"
        
        assert WebDriverWait(driver, 12).until(EC.visibility_of_element_located(Locators.main_order_button)) # Ждем кнопку "Оформить заказ" на главной странице
        # Тест проходит PASSED 


    # Тест - ОР- вход через кнопку "Войти" в форме регистрации
    def test_registration_login_button_entrance(self, open_register_page):
        driver = open_register_page # Вызов фикстуры открытия страницы регистрации
        
        WebDriverWait(driver, 12).until(EC.visibility_of_element_located(Locators.registration_button)) # Ждем кнопку "Зарегистрироваться" на странице регистрации
        driver.find_element(*Locators.registration_login_button).click() # Жмем кнопку "Войти" на странице регистрации

        WebDriverWait(driver, 12).until(EC.visibility_of_element_located(Locators.enter_login_button)) # Ждем кнопку "Войти" на странице входа
        driver.find_element(*Locators.enter_email_input).send_keys(Credentials.my_email) # Вносим Email (постоянный)
        driver.find_element(*Locators.enter_password_input).send_keys(Credentials.my_password) # Вносим Password (постоянный)
        driver.find_element(*Locators.enter_login_button).click() # Жмем кнопку "Войти"
        
        assert WebDriverWait(driver, 12).until(EC.visibility_of_element_located(Locators.main_order_button)) # Ждем кнопку "Оформить заказ" на главной странице
        # Тест проходит PASSED 


    # Тест на вход через кнопку "Войти" в форме восстановления пароля
    def test_recover_enter_button_entrance_(self, open_recovery_pass_page):
        driver = open_recovery_pass_page # Вызов фикстуры открытия страницы восстановления пароля

        WebDriverWait(driver, 12).until(EC.visibility_of_element_located(Locators.recover_button)) # Ждем кнопку "Восстановить" на странице восстановления пароля
        driver.find_element(*Locators.registration_login_button).click() # Жмем кнопку "Войти" на странице восстановления пароля
        
        WebDriverWait(driver, 12).until(EC.visibility_of_element_located(Locators.enter_login_button)) # Ждем кнопку "Войти" на странице входа
        driver.find_element(*Locators.enter_email_input).send_keys(Credentials.my_email) # Вносим Email (постоянный)
        driver.find_element(*Locators.enter_password_input).send_keys(Credentials.my_password) # Вносим Password (постоянный)
        driver.find_element(*Locators.enter_login_button).click() # Жмем кнопку "Войти"
        
        assert WebDriverWait(driver, 12).until(EC.visibility_of_element_located(Locators.main_order_button)) # Ждем кнопку "Оформить заказ" на главной странице
        # Тест проходит PASSED 
