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

    def select_side_item_value(self, SelectValue, SideBarItem):
        Side_item = f"//ul[@class='nav nav-pills nav-sidebar flex-column nav-legacy']//a[@href='#' and @class='nav-link']//p[contains(text(),'{SideBarItem}')]"
        self.driver.find_element(By.XPATH, Side_item).click()
        time.sleep(1)
        selectValue = f"//p[text()='{SelectValue}']"
        self.driver.find_element(By.XPATH, selectValue).click()
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
