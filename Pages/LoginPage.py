import time
from telnetlib import EC
from selenium.webdriver.common.by import By


class LoginPage:
    username_by_id = "Email"
    password_by_name = "Password"
    login_btn_by_xpath = "//button[text()='Log in']"

    def __init__(self, driver):
        self.driver = driver

    def setUsername(self, username):
        self.driver.find_element(By.ID, self.username_by_id).clear()
        self.driver.find_element(By.ID, self.username_by_id).send_keys(username)

    def setPassword(self, password):
        self.driver.find_element(By.NAME, self.password_by_name).clear()
        self.driver.find_element(By.NAME, self.password_by_name).send_keys(password)

    def clickOnLogin(self):
        self.driver.find_element(By.XPATH, self.login_btn_by_xpath).click()
        time.sleep(3)
