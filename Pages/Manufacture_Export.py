import time

from selenium.webdriver.common.by import By


class ManufactureExport:
    export_xpath = "//*//button[normalize-space()='Export']"
    dropdown_xpath = "//button[@class='btn btn-success dropdown-toggle']"

    # exp_xml_xpath = "//a[@href='/Admin/Manufacturer/ExportXml']"
    # exp_excel_xpath = "//a[@href='/Admin/Manufacturer/ExportXlsx']"

    def __init__(self, driver):
        self.driver = driver

    def count_table_row(self):
        now_of_row = self.driver.find_element(By.XPATH, "//table[contains(@id,'grid')]//tbody//tr")
        return len(now_of_row)

    def count_table_col(self):
        now_of_col = self.driver.find_element(By.XPATH, "//table[contains(@id,'grid')]//tbody//tr[1]//td")
        return len(now_of_col)

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

    def search_by_name(self, value):
        self.driver.find_element(By.XPATH, "//input[@id='SearchManufacturerName']").send_keys(value)

    def i_click_on_search_btn(self):
        self.driver.find_element(By.XPATH, "//button[contains(@id,'search')]").click()

    def i_see_search_result_by_name(self, value):
        result = False
        for r in range(1, self.count_table_row() + 1):
            table = self.driver.find_element(By.XPATH, "//table[contains(@id,'grid')]")
            name = table.find_element(By.XPATH, "//table[contains(@id,'grid')]//tbody//tr[" + str(r) + "]//td[2]").text
            if name == value:
                result = True
                break
        return result
