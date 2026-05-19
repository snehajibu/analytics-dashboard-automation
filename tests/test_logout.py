import pytest

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.login_page import LoginPage


@pytest.mark.regression
def test_logout(driver):

    driver.get(
        "https://opensource-demo.orangehrmlive.com/"
    )

    login_page = LoginPage(driver)

    login_page.login(
        "Admin",
        "admin123"
    )

    wait = WebDriverWait(driver, 10)

    profile_menu = wait.until(
        EC.element_to_be_clickable(
            (By.CLASS_NAME, "oxd-userdropdown-tab")
        )
    )

    profile_menu.click()
    print("Profile menu clicked")
    
    logout_button = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//a[contains(@href, 'logout')]")
        ) 
    )

    logout_button.click()

    wait.until(
        EC.url_contains("login")
    )

    assert "login" in driver.current_url.lower()