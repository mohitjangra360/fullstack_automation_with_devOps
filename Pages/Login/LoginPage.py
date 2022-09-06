from telnetlib import EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    username_by_name = "Email"
    password_by_name = "Password"
    login_btn_by_class = "button-1 login-button"

    def __init__(self, driver):
        self.driver = driver

    def setUsername(self, username):
        self.driver.find_element(By.NAME, self.username_by_name).clear()
        self.driver.find_element(By.NAME, self.username_by_name).send_keys(username)

    def setPassword(self, password):
        self.driver.find_element(By.NAME, self.password_by_name).clear()
        self.driver.find_element(By.NAME, self.password_by_name).send_keys(password)

    def clickOnLogin(self):
        self.driver.find_element(By.CLASS_NAME, self.login_btn_by_class).click()

