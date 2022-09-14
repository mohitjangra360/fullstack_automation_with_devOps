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

