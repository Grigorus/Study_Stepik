from selenium import webdriver
import time

options = webdriver.ChromeOptions()
options.headless = False
#options.headless = True
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/"
                     "91.0.4472.106 Safari/537.36")
browser = webdriver.Chrome(executable_path='C:/Users/GRIGORUS_EN/pitonism/'
                                           'chromedriver_win32/chromedriver.exe', options=options)


try:
    link = "http://suninjuly.github.io/registration2.html"

    browser.get(link)

    first_name_input_field = browser.find_element_by_css_selector('div.first_block [class="form-control first"]')
    last_name_input_field = browser.find_element_by_css_selector('div.first_block [class="form-control second"]')
    email_input_field = browser.find_element_by_css_selector('div.first_block [class="form-control third"]')
    
    first_name_input_field.send_keys('John')
    last_name_input_field.send_keys('Doe')
    email_input_field.send_keys('jd@example.com')

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    time.sleep(1)
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    welcome_text = welcome_text_elt.text

    assert "Congratulations! You have successfully registered!" == welcome_text
finally:
    time.sleep(10)
    browser.quit()