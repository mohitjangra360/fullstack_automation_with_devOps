import time

from selenium.webdriver.common.by import By

class Import:

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

        Import_Button = f"//div[@class='float-right']//*[text()[contains(.,'{value}')]]"
        display_button = self.driver.find_element(By.XPATH, Import_Button).is_displayed()
        if display_button == True:
            assert True
        else:
            assert False

    def user_should_able_to_click_Import_Button(self, value):

        Import_Button = f"//div[@class='float-right']//*[text()[contains(.,'{value}')]]"
        self.driver.find_element(By.XPATH, Import_Button).click()
        time.sleep(2)

        self.driver.find_element(By.XPATH, "//div[@id='importexcel-window']//input[@id='importexcelfile']").click()
        time.sleep(2)

