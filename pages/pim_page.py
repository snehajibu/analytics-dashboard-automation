from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils.logger import get_logger

class PimPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)
        self.logger = get_logger()

    # Locators

    pim_menu = (By.XPATH, "//span[normalize-space()='PIM']")
    employee_name_input = (By.XPATH, "(//input[contains(@placeholder,'Type for hints')])[1]")
    search_button = (By.CSS_SELECTOR, "button[type='submit']")
    employee_table = (By.CLASS_NAME, "oxd-table-body")
   
    #Actions

    def navigate_to_pim(self):
        self.logger.info("Navigate to PIM module")

        pim = self.wait.until(EC.visibility_of_element_located(self.pim_menu))
        self.driver.execute_script("arguments[0].click();",pim)

        self.wait.until(EC.presence_of_element_located(self.employee_name_input))

    def search_employee(self, employee_name):
        self.logger.info(f"Searching employee: {employee_name}")

        employee_input = self.wait.until(EC.visibility_of_element_located(self.employee_name_input))
        employee_input.clear()
        employee_input.send_keys(employee_name)

        search_btn = self.driver.find_element(*self.search_button)

        search_btn.click()

    def is_employee_table_displayed(self):
        table = self.wait.until(EC.visibility_of_element_located(self.employee_table))
        return table.is_displayed()
    

