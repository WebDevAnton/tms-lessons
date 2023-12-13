import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys

@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_find_love_syn(browser):
    browser.get("https://www.thesaurus.com/")

    search_box = browser.find_element(By.XPATH, "//*[@id='global-search']")
    search_box.send_keys("love")
    search_box.send_keys(Keys.ENTER)