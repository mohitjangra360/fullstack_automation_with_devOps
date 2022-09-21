import time

from selenium.webdriver.common.by import By

class Delete:

    def __init__(self, driver):
        self.driver = driver

    def go_to_childitem_page(self, childitem, parentitem):
        ParentItem = f"//ul[@class='nav nav-pills nav-sidebar flex-column nav-legacy']//a[@href='#' and @class='nav-link']//p[contains(text(),'{parentitem}')]"
        self.driver.find_element(By.XPATH, ParentItem).click()
        time.sleep(1)
        childitem = f"//p[normalize-space()='{childitem}']"
        self.driver.find_element(By.XPATH, childitem).click()
        time.sleep(3)

    def user_should_able_to_see_Delete_Button(self, value):

        Button = f"//div[@class='float-right']//*[text()[contains(.,'{value}')]]"
        display_button = self.driver.find_element(By.XPATH, Button).is_displayed()
        if display_button == True:
            assert True
        else:
            assert False

    def user_should_able_to_click_Delete_Button(self, value):

        if 'dataTables_empty' in self.driver.page_source:
            Button = f"//div[@class='float-right']//*[text()[contains(.,'{value}')]]"
            self.driver.find_element(By.XPATH, Button).click()
            time.sleep(3)
        else:
            Checkbox_values = "//tbody//input[@class='checkboxGroups']"
            get_checkboxvalues = self.driver.find_elements(By.XPATH, Checkbox_values)
            Value_list=[]

            for all_value in get_checkboxvalues:
                value_text = all_value.get_attribute('value')
                Value_list.append(value_text)
                print(Value_list)

            time.sleep(2)
            self.driver.find_element(By.XPATH, f"//tbody//input[@value= {Value_list[0]}]").click()
            time.sleep(2)

            Button = f"//div[@class='float-right']//*[text()[contains(.,'{value}')]]"
            self.driver.find_element(By.XPATH, Button).click()
            time.sleep(5)

    def user_should_able_to_click_YES_delete_popup(self):
        Click_YES = "//div[@class='modal-content']//div[@class='modal-footer']//button[contains(text(), 'Yes')]"
        Click_OK = "//div[@id='nothingSelectedAlert-action-alert']//div[@class='modal-footer']//span[contains(text(), 'Ok')]"

        nothing_selected_popUP = "//div[@id='nothingSelectedAlert-info']"
        self.driver.find_element(By.XPATH, Click_YES).click()
        time.sleep(2)

        if nothing_selected_popUP in self.driver.page_source:
            self.driver.find_element(By.XPATH, Click_OK).click()
        else:
            print("deleted done")
