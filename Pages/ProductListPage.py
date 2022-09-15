import time

from selenium.webdriver.common.by import By


class ProductListPage:

    def __init__(self, driver):
        self.driver = driver

    def i_should_see_product_column(self):
        # to identify headers
        column_list = self.driver.find_elements(By.XPATH, "//div[@class='dataTables_scrollHead']//th")
        print(len(column_list))

        # to identify rows in table body
        rows_list = self.driver.find_elements(By.XPATH, "//tbody//tr")
        print(len(rows_list))

    def click_on_import(self):
        self.driver.find_element(By.XPATH, "//button[@name='importexcel']").click()
        time.sleep(3)
        # self.driver.getWindowHandles()
        # self.driver.switchTo().window(handle);

    def click_on_choose_file(self):
        self.driver.find_element(By.XPATH, "//div[@id='importexcel-window']//form//input[@id='importexcelfile']").send_keys('D:\Automation\\fullstack_automation_with_devOps\\test.py')
        time.sleep(5)


