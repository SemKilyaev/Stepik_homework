import pytest
import time
from selenium import webdriver

def is_element_present(browser, xpath):
    try:
        browser.implicitly_wait(10)
        browser.find_element_by_xpath(xpath)
        return True
    except:
        return False

def test_add_button(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    xpath = "//button[@class='btn btn-lg btn-primary btn-add-to-basket']"
    browser.get(link)
    time.sleep(5)
    assert is_element_present(browser, xpath) == True, "Element do not find"