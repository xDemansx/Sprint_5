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


# Тесты навигации по сайту
class TestSiteBurgersNavigation:


    # Тест - ОР - переход в личный кабинет по клику на "Личный кабинет"
    def test_navigate_to_main_account(self, open_main_page_login_page):
        driver = open_main_page_login_page # Вызов фикстуры входа по кнопке «Войти в аккаунт» на главной странице сайта

        WebDriverWait(driver, 12).until(EC.visibility_of_element_located(Locators.main_order_button)) # Ждем кнопку "Оформить заказ" на главной странице
        driver.find_element(*Locators.main_account_button).click() # Жмем кнопку "Личный кабинет" на главной странице

        assert WebDriverWait(driver, 12).until(EC.visibility_of_element_located(Locators.lk_exit_button)) # Ждем кнопку "Выход" в Личном кабинете
        # Тест проходит PASSED


    # Тест - ОР - переход из личного кабинета в конструктор по клику на "Конструктор"
    def test_navigate_to_constructor_from_main_account(self, open_main_page_login_page):
        driver = open_main_page_login_page # Вызов фикстуры входа по кнопке «Войти в аккаунт» на главной странице сайта

        WebDriverWait(driver, 12).until(EC.visibility_of_element_located(Locators.main_order_button)) # Ждем кнопку "Оформить заказ" на главной странице
        driver.find_element(*Locators.main_account_button).click() # Жмем кнопку "Личный кабинет" на главной странице

        WebDriverWait(driver, 12).until(EC.visibility_of_element_located(Locators.lk_exit_button)) # Ждем кнопку "Выход" в Личном кабинете
        driver.find_element(*Locators.main_constructor_button).click() # Жмем кнопку "Конструктор" в Личном кабинете

        assert WebDriverWait(driver, 12).until(EC.visibility_of_element_located(Locators.main_order_button)) # Ждем кнопку "Оформить заказ" в конструкторе
        # Тест проходит PASSED


    # Тест - ОР - переход из личного кабинета в конструктор по клику на логотип Stellar Burger
    def test_navigate_to_constructor_from_main_logo(self, open_main_page_login_page):
        driver = open_main_page_login_page # Вызов фикстуры входа по кнопке «Войти в аккаунт» на главной странице сайта

        WebDriverWait(driver, 12).until(EC.visibility_of_element_located(Locators.main_order_button)) # Ждем кнопку "Оформить заказ" на главной странице
        driver.find_element(*Locators.main_account_button).click() # Жмем кнопку "Личный кабинет" на главной странице

        WebDriverWait(driver, 12).until(EC.visibility_of_element_located(Locators.lk_exit_button)) # Ждем кнопку "Выход" в Личном кабинете
        driver.find_element(*Locators.main_logo_button).click() # Жмем кнопку логотипа "Stellar Burger" в Личном кабинете

        assert WebDriverWait(driver, 12).until(EC.visibility_of_element_located(Locators.main_order_button)) # Ждем кнопку "Оформить заказ" в конструкторе
        # Тест проходит PASSED


    # Тест - ОР - выход из аккаунта
    def test_exit_from_account(self, open_main_page_login_page):
        driver = open_main_page_login_page

        WebDriverWait(driver, 12).until(EC.visibility_of_element_located(Locators.main_order_button)) # Ждем кнопку "Оформить заказ" на главной странице
        driver.find_element(*Locators.main_account_button).click() # Жмем кнопку "Личный кабинет" на главной странице

        WebDriverWait(driver, 12).until(EC.visibility_of_element_located(Locators.lk_exit_button)) # Ждем кнопку "Выход" в Личном кабинете
        driver.find_element(*Locators.lk_exit_button).click() # Жмем кнопку "Выход" в Личном кабинете

        assert WebDriverWait(driver, 12).until(EC.visibility_of_element_located(Locators.enter_login_button)) # Ждем кнопку "Войти" в странице входа
        # Тест проходит PASSED
        