import random
import string

from selenium.webdriver.common.by import By


class Add_Customer:
    customer_item_by_xpath = "//a[@href='#']//p[contains(text(),'Customers')]"
    customer_link_by_xpath = "//a[@href='/Admin/Customer/List']//p"
    add_new_by_xpath = "//a[@href='/Admin/Customer/Create']"
    email_by_xpath = "//input[@id='Email']"
    password_by_xpath = "//input[@id='Password']"
    firstname_by_xpath = "//input[@id='FirstName']"
    lastname_by_xpath = "//input[@id='LastName']"

    def __init__(self, driver):
        self.driver = driver

    def click_on_customer_item(self):
        self.driver.find_element(By.XPATH, self.customer_item_by_xpath).click()

    def click_on_menu_link_item_for_cust(self):
        self.driver.find_element(By.XPATH, self.customer_link_by_xpath).click()

    def click_on_add_new_cust_btn(self):
        self.driver.find_element(By.XPATH, self.add_new_by_xpath).click()

    def set_mail_for_cust(self):
        self.driver.find_element(By.XPATH, self.email_by_xpath).send_keys(email)

    def set_password(self, password):
        self.driver.find_element(By.XPATH, self.password_by_xpath).send_keys(password)

    def set_firstname(self, firstname):
        self.driver.find_element(By.XPATH, self.firstname_by_xpath).send_keys(firstname)

    def set_lastname(self, lastname):
        self.driver.find_element(By.XPATH, self.lastname_by_xpath).send_keys(lastname)




def random_email(size=10, char=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(char) for x in range(size))


email = random_email() + "@gmail.com"
