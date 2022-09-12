from selenium.webdriver.common.by import By

class Search:
    Dashboard_Xpath = "//*[@class='content-header']"
    Searchbar_Xpath = "//*[@id='search-box']//input[@type='text']"

    def __init__(self, driver):
        self.driver = driver

    def user_should_see_searchbar(self):
        searchbar_text = self.driver.find_element(By.XPATH, self.Searchbar_Xpath ).is_displayed()
        if searchbar_text == True:
            assert True
        else:
            assert False

    def user_should_click_searchbar(self):
        self.driver.find_element(By.XPATH, self.Searchbar_Xpath).click()
        self.driver.find_element(By.XPATH, self.Searchbar_Xpath).sendkeys("pl")

