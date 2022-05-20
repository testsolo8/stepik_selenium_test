import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options




def test_practic():
    browser = webdriver.Chrome()
    browser.get("http://selenium1py.pythonanywhere.com/")
    link = browser.find_element_by_css_selector("#login_link")
    link.click()
    login_url = browser.current_url
    sub_string = 'login'
    assert sub_string in login_url



