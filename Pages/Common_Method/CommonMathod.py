import time
from telnetlib import EC
from selenium.webdriver.common.by import By


class CommonMethod:
    username_by_id = "Email"
    password_by_name = "Password"
    login_btn_by_xpath = "//button[text()='Log in']"

    def __init__(self, driver):
        self.driver = driver

    def i_should_see(self, textValue):
        xpath = f"//*[contains(text(),'{textValue}')]"
        visible = self.driver.find_element(By.XPATH, xpath).is_displayed()
        if visible == True:
            assert True
        else:
            assert False

    def i_should_see_input_field(self, val, locator):
        visible = self.driver.find_element(By.XPATH, f"//input[@{locator}='{val}']").is_displayed()
        if visible == True:
            assert True
        else:
            assert False

    def i_should_see_checkbox(self, value, locator):
        checkbox = self.driver.find_element(By.XPATH, f"//input[@{locator}='{value}' and @type='checkbox']")
        checkbox_visible = checkbox.is_displayed()
        if checkbox_visible == True:
            assert True
        else:
            assert False

    def i_should_see_button(self, value, locator):
        btn_xpath = f"//button[contains(@{locator},'{value}')]"
        btn = self.driver.find_element(By.XPATH, btn_xpath)
        btn_visible = btn.is_displayed()
        if btn_visible == True:
            assert True
        else:
            assert False
