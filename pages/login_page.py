from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # Locators
    username_input = (
        By.CSS_SELECTOR,
        "input[name='username']"
    )

    password_input = (
        By.CSS_SELECTOR,
        "input[name='password']"
    )

    login_button = (
        By.CSS_SELECTOR,
        "button[type='submit']"
    )

    error_message = (
        By.CLASS_NAME,
        "oxd-alert-content-text"
    )

    # Actions
    def enter_username(self, username):

        username_field = self.wait.until(
            EC.visibility_of_element_located(
                self.username_input
            )
        )

        username_field.send_keys(username)

    def enter_password(self, password):

        password_field = self.driver.find_element(
            *self.password_input
        )

        password_field.send_keys(password)

    def click_login(self):

        login_btn = self.driver.find_element(
            *self.login_button
        )

        login_btn.click()

    def get_error_message(self):

        error = self.wait.until(
            EC.visibility_of_element_located(
                self.error_message
            )
        )

        return error.text
    
    def login(self, username, password):

        self.enter_username(username)

        self.enter_password(password)

        self.click_login()