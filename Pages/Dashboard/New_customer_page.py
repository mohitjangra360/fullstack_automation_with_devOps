from selenium.webdriver.common.by import By


class NewCustomerPage:

    def __init__(self, driver):
        self.driver = driver

    # def i_should_see_expand_collapes_btn(self, value, locator):
    #     btn = self.driver.find_element(By.XPATH, f"(//button[contains(@{locator},'{value}')])[6]").is_displayed()
    #     if btn == True:
    #         assert True
    #     else:
    #         assert False

    def i_should_see_graph(self):
        graph=self.driver.find_element(By.XPATH,"//canvas[@id='customer-statistics-chart')]").is_displayed()
        if graph ==True:
            assert True
        else:
            assert False



    def i_should_see_btn(self):
        btn=self.driver.find_element(By.XPATH,"(//button[contains(@class,'btn-tool')])[6]").is_displayed()
        if btn ==True:
            assert True
        else:
            assert False
