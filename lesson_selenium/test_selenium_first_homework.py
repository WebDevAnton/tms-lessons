import pytest
from selenium import webdriver


class TestSelenium:
    @pytest.mark.parametrize("url, page_title",
    [
    ("https://www.amazon.com/", "Amazon"),
    ("https://www.apple.com/", "Apple"),
    ("https://www.google.com/", "Google")
    ])
    def test_page_title(self, url, page_title):
        if "Amazon" in url:
            driver = webdriver.Firefox()
        elif "Apple" in url:
            driver = webdriver.Safari()
        else:
            driver = webdriver.Chrome()
        driver.get(url)
        actual_title = driver.title
        assert page_title.lower() in actual_title.lower(), f"Ожидали '{page_title}', но получили '{actual_title}'"
        driver.save_screenshot(f"{page_title}_screenshot.png")
