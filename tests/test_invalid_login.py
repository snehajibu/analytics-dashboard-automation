from pages.login_page import LoginPage
from utils.screenshot_utils import take_screenshot


def test_invalid_login(driver):

    driver.get(
        "https://opensource-demo.orangehrmlive.com/"
    )

    login_page = LoginPage(driver)

    login_page.login("wronguser", "wrongpassword")



    try:

        assert "Invalid credentials" in (
        login_page.get_error_message()
        )

    except AssertionError:

        take_screenshot(driver, "invalid_login_failure")

        raise
    