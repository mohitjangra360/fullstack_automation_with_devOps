import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Delete:

    def __init__(self, driver):
        self.driver = driver

    def go_to_product_page(self, childitem, parentitem):
        ParentItem = f"//ul[@class='nav nav-pills nav-sidebar flex-column nav-legacy']//a[@href='#' and @class='nav-link']//p[contains(text(),'{parentitem}')]"
        self.driver.find_element(By.XPATH, ParentItem).click()
        time.sleep(1)
        childitem = f"//p[normalize-space()='{childitem}']"
        self.driver.find_element(By.XPATH, childitem).click()
        time.sleep(3)

    def user_should_able_to_see_Import_Button(self, value):

        Button = f"//div[@class='float-right']//*[text()[contains(.,'{value}')]]"
        display_button = self.driver.find_element(By.XPATH, Button).is_displayed()
        if display_button == True:
            assert True
        else:
            assert False

    def user_should_able_to_click_Import_Button(self, value):

        self.driver.find_element(By.XPATH, "//input[@value='1']").click()

        Button = f"//div[@class='float-right']//*[text()[contains(.,'{value}')]]"
        self.driver.find_element(By.XPATH, Button).click()
        #time.sleep(5)

        element = WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "modal-dialog")))

       # modal_container = self.driver.find_element(By.XPATH, "//div[@class='modal-dialog']")

