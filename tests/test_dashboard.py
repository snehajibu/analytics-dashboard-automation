from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.login_page import LoginPage
import pytest

@pytest.mark.smoke
def test_login(driver):

    driver.get("https://opensource-demo.orangehrmlive.com/")

    login_page = LoginPage(driver)

    login_page.login("Admin", "admin123")
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,"//span[normalize-space()='PIM']")))

    wait = WebDriverWait(driver, 10)

    wait.until(EC.url_contains("dashboard"))
    assert "dashboard" in driver.current_url.lower()