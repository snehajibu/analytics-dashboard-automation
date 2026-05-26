from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.logger import get_logger

class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.logger = get_logger()

    # Locators
    username_input = (By.CSS_SELECTOR,"input[name='username']")
    password_input = (By.CSS_SELECTOR,"input[name='password']")
    login_button = (By.CSS_SELECTOR,"button[type='submit']")
    error_message = (By.CLASS_NAME,"oxd-alert-content-text")

    # Actions
    def enter_username(self, username):
        self.logger.info(f"Entering username {username}")
        username_field = self.wait.until(EC.visibility_of_element_located(self.username_input))
        username_field.send_keys(username)

    def enter_password(self, password):
        self.logger.info("Entering password")
        password_field = self.driver.find_element(*self.password_input)
        password_field.send_keys(password)

    def click_login(self):
        self.logger.info("Clicking login button")
        login_btn = self.driver.find_element(*self.login_button)
        login_btn.click()

    def get_error_message(self):
        error = self.wait.until(EC.visibility_of_element_located(self.error_message))
        return error.text
    
    def login(self, username, password):
        self.logger.info("Starting login workflow")
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()
