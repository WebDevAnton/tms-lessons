import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class myfinby:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def open_site(self, url):
        self.driver.get(url)

    def card_section(self):
        card_section = driver.find_element(By.XPATH, "//*[@href ='/cards']")
        webdriver.ActionChains(driver).move_to_element(card_section).perform()

    def click_on_card_link(self):
        card_link = driver.find_element(By.XPATH, "//*[text()='Онлайн оформление карты']/..//*[@alt='Красная карта 2.0']")
        card_link.click()

    def switch_to_new_window(self):
        driver.switch_to.window(driver.window_handles[-1])

    def enter_phone_n(self):
        ph_number_field = driver.find_element(By.XPATH, "//input[@type='tel']")
        ph_number_field.send_keys("299402265")

    def click_on_confirm_button(self):
        conf_button = driver.find_element(By.XPATH, "//*[text()='Подтвердить']")
        conf_button.click()

@pytest.fixture()
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--window-size=1920,1080")
    with webdriver.Chrome(options) as driver:
        yield driver

class Testmyfinby:
    def test_myfinby(self, driver):
        myfin_homework = myfinby(driver)
        myfin_homework.open_site("https://myfin.by/")
        myfin_homework.card_section()
        myfin_homework.click_on_card_link()
        myfin_homework.switch_to_new_window()
        myfin_homework.enter_phone_n("299402265")
        myfin_homework.click_on_confirm_button()
