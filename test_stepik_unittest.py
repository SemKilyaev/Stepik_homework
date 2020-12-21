import time  
import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


class TestStepik(unittest.TestCase):

    input_first_name = "//div[@class='first_block']/div[@class='form-group first_class']/input "
    input_last_name = "//div[@class='first_block']/div[@class='form-group second_class']/input "
    input_email = "//div[@class='first_block']/div[@class='form-group third_class']/input"

    link1 = "http://suninjuly.github.io/registration1.html"
    link2 = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome(executable_path=ChromeDriverManager().install())



    def test_stepik_tru(self):

        self.browser.get(self.link1)

            #Kод, который заполняет обязательные поля
    
        self.browser.find_element_by_xpath("//div[@class='first_block']/div[@class='form-group first_class']/input ").send_keys("Name")
        self.browser.find_element_by_xpath("//div[@class='first_block']/div[@class='form-group second_class']/input ").send_keys("Secondname")
        self.browser.find_element_by_xpath("//div[@class='first_block']/div[@class='form-group third_class']/input").send_keys("test@test.com")

        # Отправляем заполненную форму
        button = self.browser.find_element_by_css_selector("button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = self.browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        a = ("Congratulations! You have successfully registered!" == welcome_text)

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertTrue(a)

        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(5)
        # закрываем браузер после всех манипуляций
        self.browser.quit()


    def test_stepik_falce(self):

        self.browser.get(self.link2)

            #Kод, который заполняет обязательные поля
    
        self.browser.find_element_by_xpath("//div[@class='first_block']/div[@class='form-group first_class']/input ").send_keys("Name")
        self.browser.find_element_by_xpath("//div[@class='first_block']/div[@class='form-group second_class']/input ").send_keys("Secondname")
        self.browser.find_element_by_xpath("//div[@class='first_block']/div[@class='form-group third_class']/input").send_keys("test@test.com")

        # Отправляем заполненную форму
        button = self.browser.find_element_by_css_selector("button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = self.browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        a = ("Congratulations! You have successfully registered!" == welcome_text)

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertTrue(a)

        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(5)
        # закрываем браузер после всех манипуляций
        self.browser.quit()

if __name__ == '__main__':
    unittest.main()
    