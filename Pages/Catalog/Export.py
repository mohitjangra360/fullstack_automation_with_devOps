from selenium.webdriver.common.by import By


class Export:
    Export_Xpath = "(//*[text()[contains(., 'Export')]])[1]"
    Export_dropdown_Xpath = "//button[contains(@class,'dropdown-toggle')]"

    def __init__(self, driver):
        self.driver = driver

    def user_should_see_export(self):
        exp = self.driver.find_element(By.XPATH, self.Export_Xpath).is_displayed()
        if exp == True:
            assert True
        else:
            assert False

    def user_should_click_export(self):

        self.driver.find_element(By.XPATH, self.Export_dropdown_Xpath).click()
