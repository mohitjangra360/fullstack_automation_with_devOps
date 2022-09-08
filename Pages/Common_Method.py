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
