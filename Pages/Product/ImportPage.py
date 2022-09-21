import time

from selenium.webdriver.common.by import By


class Import:

    def __init__(self, driver):
        self.driver = driver

    def go_to_childitem_page(self, childitem, parentitem):
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

    def user_should_able_to_see_import_popup(self, value):
        POP_UP_DISPLAY = self.driver.find_element(By.XPATH,
                                                  f"//div[@class='modal-dialog']//div//div//h4[contains(text(),'{value}')]").is_displayed()
        if POP_UP_DISPLAY == True:
            assert True
        else:
            assert False

    def user_should_able_to_select_import_file(self, path):
        self.driver.find_element(By.XPATH, "//div[@class='modal-dialog']//form//input[@id='importexcelfile']").send_keys(f'{path}')
        time.sleep(2)

    def user_should_able_to_click_button_of_Import(self, value):
        self.driver.find_element(By.XPATH, f"//div[@class='modal-footer']//button[contains(.,'{value}')]").click()

    def user_should_able_to_see_error_message_of_Import(self, childitem):
        ErrorMessage_1 ='×\nFor security purposes, the feature you have requested is not available on the demo site.'
        ErrorMessage_2 ='×\nPlease upload a file'
        ErrorMessage_3 ='×\nSequence contains no elements'
        SuccessfulMessage =f'×\n{childitem} have been imported successfully.'

        Error_POPUP_text = "//div[@class='alert alert-danger alert-dismissable']"
        Success_popup_text = "//div[@class='alert alert-success alert-dismissable']"

        if 'alert alert-danger alert-dismissable' in self.driver.page_source:
            geterrorValue = self.driver.find_element(By.XPATH, Error_POPUP_text)
            item_error_text = geterrorValue.text

            if item_error_text == ErrorMessage_1:
                assert True
            elif item_error_text == ErrorMessage_2:
                assert True
            elif item_error_text == ErrorMessage_3:
                assert True
            else:
                assert False
        else:
            getsuccessValue = self.driver.find_element(By.XPATH, Success_popup_text)
            item_success_text = getsuccessValue.text

            if item_success_text == SuccessfulMessage:
                assert True
            else:
                assert False



