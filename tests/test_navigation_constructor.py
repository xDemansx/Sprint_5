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


# Тесты навигации по разделам Конструктора
class TestConstructorBurgersNavigation:
    
    # Тест - ОР - переход к разделу "Булки" в конструкторе
    def test_constructor_buns(self, open_main_page):
        driver = open_main_page # Вызов фикстуры открытия главной страницы сайта

        WebDriverWait(driver, 12).until(EC.visibility_of_element_located(Locators.main_enter_button)) # Ждем кнопку «Войти в аккаунт» на главной странице сайта
        driver.find_element(*Locators.constructor_stuff).click() # Жмем раздел "Начинки" в констукторе

        WebDriverWait(driver, 12).until(EC.visibility_of_element_located(Locators.constructor_active_press)) # Ждем активную кнопку Конструктора
        driver.find_element(*Locators.constructor_buns).click() # Жмем раздел "Булки" в констукторе
        
        constructor_element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.constructor_active_press)) # Активная кнопка
        
        assert constructor_element.is_displayed() # Ждем отображения активной кнопки
        assert Locators.constructor_buns_text in constructor_element.text # Сравниваем текст 'Булки' с текстом активной кнопки
        # Тест проходит PASSED


    # Тест - ОР - переход к разделу "Соусы" в конструкторе
    def test_constructor_sauces(self, open_main_page):
        driver = open_main_page # Вызов фикстуры открытия главной страницы сайта

        WebDriverWait(driver, 12).until(EC.visibility_of_element_located(Locators.main_enter_button)) # Ждем кнопку «Войти в аккаунт» на главной странице сайта
        driver.find_element(*Locators.constructor_sauces).click() # Жмем раздел "Соусы" в констукторе

        constructor_element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.constructor_active_press)) # Активная кнопка

        assert constructor_element.is_displayed() # Ждем отображения активной кнопки
        assert Locators.constructor_sauces_text in constructor_element.text # Сравниваем текст 'Соусы' с текстом активной кнопки
        # Тест проходит PASSED

    # Тест - ОР - переход к разделу "Начинки" в конструкторе
    def test_constructor_stuff(self, open_main_page):
        driver = open_main_page # Вызов фикстуры открытия главной страницы сайта

        WebDriverWait(driver, 12).until(EC.visibility_of_element_located(Locators.main_enter_button)) # Ждем кнопку «Войти в аккаунт» на главной странице сайта
        driver.find_element(*Locators.constructor_stuff).click() # Жмем раздел "Начинки" в констукторе

        constructor_element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.constructor_active_press)) # Активная кнопка

        assert constructor_element.is_displayed() # Ждем отображения активной кнопки
        assert Locators.constructor_stuff_text in constructor_element.text # Сравниваем текст 'Начинки' с текстом активной кнопки
        # Тест проходит PASSED
