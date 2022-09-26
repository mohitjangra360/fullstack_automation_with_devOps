import time
from telnetlib import EC
from selenium.webdriver.common.by import By


class CommonMethod:

    def __init__(self, driver):
        self.driver = driver

    def i_should_see(self, textValue):
        xpath = f"//*[contains(text(),'{textValue}')]"
        visible = self.driver.find_element(By.XPATH, xpath).is_displayed()
        if visible == True:
            assert True
        else:
            assert False

    def i_should_see_input_field(self, value, locator):
        input = self.driver.find_element(By.XPATH, f"//input[@{locator}='{value}']").is_displayed()
        if input == True:
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

    def i_should_see_expand_collapes_btn(self, value, locator):
        btn = self.driver.find_element(By.XPATH, f"//button[contains(@{locator},'{value}')]")
        btn_status = btn.is_displayed()
        if btn_status:
            assert True

    def i_select_child_from_parent_side_menu_bar(self, childitem, parentitem):
        ParentItem = f"//ul[@class='nav nav-pills nav-sidebar flex-column nav-legacy']//a[@href='#' and @class='nav-link']//p[contains(text(),'{parentitem}')]"
        self.driver.find_element(By.XPATH, ParentItem).click()
        time.sleep(1)
        childitem = f"//p[normalize-space()='{childitem}']"
        self.driver.find_element(By.XPATH, childitem).click()
        time.sleep(3)

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

    def i_should_see_select_field(self, value, locator):
        select = self.driver.find_element(By.XPATH, f"//select[@{locator}='{value}']").is_displayed()
        if select == True:
            assert True
        else:
            assert False

    def i_am_on_page(self, page):
        if page == "Products":
            # self.driver.navigate().to()
            self.driver.open('https://admin-demo.nopcommerce.com/Admin/Category/List')

    def i_should_click_select_field(self, value, locator, select):
        self.driver.find_element(By.XPATH, f"//select[@{locator}='{value}']").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, f"//select[@{locator}='{value}']//option[contains(text(), '{select}')]").click()
        time.sleep(2)

    def i_click_search(self, button):
        self.driver.find_element(By.XPATH, f"//button[contains(., '{button}')]").click()
        time.sleep(2)