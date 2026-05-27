import pytest
from pages.login_page import LoginPage
from pages.pim_page import PimPage

@pytest.mark.skip(reason="Flaky in headless CI")
def test_employee_search(driver):
    driver.get("https://opensource-demo.orangehrmlive.com/")

    login_page = LoginPage(driver)

    login_page.login("Admin", "admin123")
    pim_page = PimPage(driver)
    pim_page.navigate_to_pim()

    pim_page.search_employee("Linda")

    assert pim_page.is_employee_table_displayed(),"Employee search results not displayed"
