import time
import math
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

ufo_answer = []

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.mark.parametrize('link', ["https://stepik.org/lesson/236895/step/1",
                                  "https://stepik.org/lesson/236896/step/1",
                                  "https://stepik.org/lesson/236897/step/1",
                                  "https://stepik.org/lesson/236898/step/1",
                                  "https://stepik.org/lesson/236899/step/1",
                                  "https://stepik.org/lesson/236903/step/1",
                                  "https://stepik.org/lesson/236904/step/1",
                                  "https://stepik.org/lesson/236905/step/1"])
def test_ufo(browser, link):
    browser.get(link)
    time.sleep(5)
    browser.find_element_by_xpath("//textarea")
    answer = math.log(int(time.time()))
    print(answer)
    time.sleep(5)
    browser.find_element_by_xpath("//textarea").send_keys(str(answer))
    browser.find_element_by_xpath("//button[text()='Отправить']").click()
    time.sleep(5)
    a = browser.find_element_by_xpath("//div/pre[@class='smart-hints__hint']").text
    if a == "Correct!":
        assert True
    else:
        ufo_answer.append(a)
        print(a)
        print(ufo_answer)
        assert False

