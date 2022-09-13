import time

from selenium.webdriver.common.by import By


class LogoutPage:

    def __init__(self, driver):
        self.driver = driver

    def logout_page_display(self):

        # hp = self.driver.find_element(By.XPATH, "/html/body/div[3]/nav/div/ul/li[3]/a").is_displayed()
        hp = self.driver.find_element(By.XPATH, "//a[contains(text(),'Logout')]").is_displayed()
        if hp:
            assert True
        else:
            assert False

    def click_on_logout_button(self):
        self.driver.find_element(By.XPATH, "/html/body/div[3]/nav/div/ul/li[3]/a").click()



