import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

@pytest.fixture()
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--window-size=1920,1080")
    with webdriver.Chrome(options) as driver:
        yield driver

def assert_element(driver, xpath, clickable=False, return_many=False):
    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located((By.XPATH, xpath)))
    wait.until(EC.visibility_of_element_located((By.XPATH, xpath)))

    if clickable:
        wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))

    if return_many:
        result = driver.find_elements(By.XPATH, xpath)
    else:
        result = driver.find_element(By.XPATH, xpath)

    return result

def click(driver, xpath):
    element = assert_element(driver, xpath, clickable=True)

    element.click()

class TestSeleniumThirdHomework:
    def test_myfin(self, driver):
        driver.get("https://myfin.by/")

        card_section = driver.find_element(By.XPATH, "//*[@href ='/cards']")
        webdriver.ActionChains(driver).move_to_element(card_section).perform()

        card_link = driver.find_element(By.XPATH, "//*[text()='Онлайн оформление карты']/..//*[@alt='Красная карта 2.0']")
        card_link.click()

        driver.switch_to.window(driver.window_handles[-1])

        ph_number_field = driver.find_element(By.XPATH, "//input[@type='tel']")
        ph_number_field.send_keys("299402265")

        conf_button = driver.find_element(By.XPATH, "//*[text()='Подтвердить']")
        conf_button.click()