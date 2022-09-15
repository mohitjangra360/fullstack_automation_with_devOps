import time

from selenium.webdriver.common.by import By


class ManufactureExport:
    export_xpath = "//*//button[normalize-space()='Export']"
    dropdown_xpath = "//button[@class='btn btn-success dropdown-toggle']"

    # exp_xml_xpath = "//a[@href='/Admin/Manufacturer/ExportXml']"
    # exp_excel_xpath = "//a[@href='/Admin/Manufacturer/ExportXlsx']"

    def __init__(self, driver):
        self.driver = driver

    def i_should_see_export_button(self):
        exp = self.driver.find_element(By.XPATH, self.export_xpath).is_displayed()
        if exp:
            assert True
        else:
            assert False

    def i_should_click_on_export_button(self):
        self.driver.find_element(By.XPATH, self.dropdown_xpath).click()
        time.sleep(10)

    def i_should_click_on_both_dropdown_list(self):
        dropdown_list_text = self.driver.find_element(By.XPATH, "//ul[@class='dropdown-menu show']//a")
        text_dropdown_list = []
        for get_text_dropdown_list in dropdown_list_text:
            hp = get_text_dropdown_list.text
            print(hp)






















