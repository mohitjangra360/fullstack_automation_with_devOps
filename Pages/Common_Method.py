import time
from telnetlib import EC
from selenium.webdriver.common.by import By


class CommonMethod:

    def __init__(self, driver):
        self.driver = driver

    def i_should_see(self, value):
        text = self.driver.find_element(By.XPATH, f"//*[contains(text(),'{value}')]").is_displayed()
        if text == True:
            assert True
        else:
            assert False

    def i_should_see_input_field(self, value, locator):
        input = self.driver.find_element(By.XPATH, f"//input[@{locator}='{value}']").is_displayed()
        if input == True:
            assert True
        else:
            assert False

    #
    # def i_should_see_input_field(self, value, locator):
    #     input = self.driver.find_element(By.XPATH, f"//input[contains(@{locator},'{value}')]").is_displayed()
    #     if input == True:
    #         assert True
    #     else:
    #         assert False
    def i_select_child_from_parent_side_menu_bar(self, childitem, parentitem):
        ParentItem = f"//ul[@class='nav nav-pills nav-sidebar flex-column nav-legacy']//a[@href='#' and @class='nav-link']//p[contains(text(),'{parentitem}')]"
        self.driver.find_element(By.XPATH, ParentItem).click()
        time.sleep(1)
        childitem = f"//p[normalize-space()='{childitem}']"
        self.driver.find_element(By.XPATH, childitem).click()
        time.sleep(3)

    def i_goto(self, X, Y, Z):
        Side_item = f"//ul[@class='nav nav-pills nav-sidebar flex-column nav-legacy']//a[@href='#' and @class='nav-link']//p[contains(text(),'{X}')]"
        self.driver.find_element(By.XPATH, Side_item).click()
        time.sleep(1)
        selectValue = f"//*[text()[contains(., '{Y}')]]"
        self.driver.find_element(By.XPATH, selectValue).click()
        time.sleep(1)
        selectValue = f"//*[text()[contains(., '{Z}')]]"
        self.driver.find_element(By.XPATH, selectValue).click()
        time.sleep(3)
