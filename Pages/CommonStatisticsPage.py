from selenium.webdriver.common.by import By


class CommonStatisticsPage:
    common_stats_By_xpath = "(//div[@class = 'card-title'])[2]"

    def __init__(self, driver):
        self.driver = driver

    def common_stats_displayed(self):
        common_stats_status = self.driver.find_element(By.XPATH, self.common_stats_By_xpath).is_displayed()
        if common_stats_status:
            assert True
        else:
            assert False
