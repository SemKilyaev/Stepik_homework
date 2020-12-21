from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time  


link1 = "http://suninjuly.github.io/registration1.html"
link2 = "http://suninjuly.github.io/registration2.html"
browser = webdriver.Chrome(executable_path=ChromeDriverManager().install())
browser.get(link2)

try: 

    #Kод, который заполняет обязательные поля
    
    input_first_name = browser.find_element_by_xpath("//div[@class='first_block']/div[@class='form-group first_class']/input ").send_keys("Name")
    input_last_name = browser.find_element_by_xpath("//div[@class='first_block']/div[@class='form-group second_class']/input ").send_keys("Secondname")
    input_email = browser.find_element_by_xpath("//div[@class='first_block']/div[@class='form-group third_class']/input").send_keys("test@test.com")

    # Отправляем заполненную форму
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
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()