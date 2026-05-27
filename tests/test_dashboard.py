from pages.login_page import LoginPage
import pytest

@pytest.mark.smoke
def test_login(driver):

    driver.get("https://opensource-demo.orangehrmlive.com/")

    login_page = LoginPage(driver)

    login_page.login("Admin", "admin123")
    assert "dashboard" in driver.current_url.lower()