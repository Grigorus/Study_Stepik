from selenium import webdriver
import time
import os
import math as math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
options = webdriver.ChromeOptions()
options.headless = True
import unittest
#options.headless = True
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/"
                     "91.0.4472.106 Safari/537.36")
browser = webdriver.Chrome(executable_path='C:/Users/PythonCoder/PycharmProjects/chromedriver.exe', options=options)


class Test3_2(unittest.TestCase):

    def test3_2valid(self):
        browser.get('http://suninjuly.github.io/registration1.html')
        # Ваш код, который заполняет обязательные поля
        browser.find_element_by_css_selector('body > div > form > div.first_block > div.form-group.first_class > input').send_keys('fffffff')
        browser.find_element_by_css_selector(
            'body > div > form > div.first_block > div.form-group.second_class > input').send_keys('fffffff')
        browser.find_element_by_css_selector(
            'body > div > form > div.first_block > div.form-group.third_class > input').send_keys('fff@ffff')
        browser.find_element_by_css_selector(
            'body > div > form > div.second_block > div.form-group.first_class > input').send_keys('777777777777777')
        browser.find_element_by_css_selector(
            'body > div > form > div.second_block > div.form-group.second_class > input').send_keys('fffffff')
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)

    def test3_2nonvalid(self):
        browser.get('http://suninjuly.github.io/registration2.html')
        # Ваш код, который заполняет обязательные поля
        browser.find_element_by_css_selector(
            'body > div > form > div.first_block > div.form-group.first_class > input').send_keys('fffffff')
        browser.find_element_by_css_selector(
            'body > div > form > div.first_block > div.form-group.second_class > input').send_keys('fffffff')
        browser.find_element_by_css_selector(
            'body > div > form > div.first_block > div.form-group.third_class > input').send_keys('fff@ffff')
        browser.find_element_by_css_selector(
            'body > div > form > div.second_block > div.form-group.first_class > input').send_keys(
            '777777777777777')
        browser.find_element_by_css_selector(
            'body > div > form > div.second_block > div.form-group.second_class > input').send_keys('fffffff')
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)

if __name__ == "__main__":
    unittest.main()





# не забываем оставить пустую строку в конце файла