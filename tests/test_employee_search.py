import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from pages.login_page import LoginPage
from pages.pim_page import PimPage

@pytest.mark.regression
def test_employee_search(driver):
    driver.get("https://opensource-demo.orangehrmlive.com/")

    login_page = LoginPage(driver)

    login_page.login("Admin", "admin123")

    pim_page = PimPage(driver)
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,"//span[normalize-space()='PIM']")))
    pim_page.navigate_to_pim()

    pim_page.search_employee("Linda")

    assert pim_page.is_employee_table_displayed(),"Employee search results not displayed"
