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

    def i_goto(self, x, y, z):
        ParentItem = f"//ul[@class='nav nav-pills nav-sidebar flex-column nav-legacy']//a[@href='#' and @class='nav-link']//p[contains(text(),'{x}')]"
        self.driver.find_element(By.XPATH, ParentItem).click()
        time.sleep(1)
        childitem = f"//*[text()[contains(.,'{y}')]]"
        self.driver.find_element(By.XPATH, childitem).click()
        time.sleep(2)
        subchilditem = f"//*[text()[contains(.,'{z}')]]"
        self.driver.find_element(By.XPATH, subchilditem).click()
        time.sleep(5)
