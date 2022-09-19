import random
import string
import time

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

    def set_gender(self, gender):
        if gender == 'Male':
            self.driver.find_element(By.XPATH, "//input[@id='Gender_Male']").click()
        elif gender == 'Female':
            self.driver.find_element(By.XPATH, "//input[@id='Gender_Female']").click()
        else:
            self.driver.find_element(By.XPATH, "//input[@id='Gender_Male']").click()


    def set_dob(self, dob):
        self.driver.find_element(By.XPATH, "//input[@id='DateOfBirth']").send_keys(dob)

    def set_customer_role(self, role):
        global listitem
        select_role = self.driver.find_element(By.XPATH, "//li[@class='k-button']//span[2]")
        if select_role.is_displayed():
            time.sleep(2)
            self.driver.find_element(By.XPATH, "//li[@class='k-button']//span[2]").click()
        self.driver.find_element(By.XPATH, "(//div[@class='k-multiselect-wrap k-floatwrap'])[2]").click()
        if role == 'Registered':
            listitem = self.driver.find_element(By.XPATH, "//li[contains(text(),'Registered')]")
            time.sleep(3)
        elif role == 'Admin':
            listitem = self.driver.find_element(By.XPATH, "//li[contains(text(),'Administrators')]")
            time.sleep(3)
        elif role == 'Forum':
            listitem = self.driver.find_element(By.XPATH, "//li[contains(text(),'Forum Moderators')]")
            time.sleep(3)
        elif role == 'Guest':
            listitem = self.driver.find_element(By.XPATH, "//li[contains(text(),'Guests')]")
            time.sleep(3)
        elif role == 'Vender':
            listitem = self.driver.find_element(By.XPATH, "//li[contains(text(),'Vendors')]")
            time.sleep(3)
        self.driver.execute_script("arguments[0].click();", listitem)


def random_email(size=10, char=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(char) for x in range(size))


email = random_email() + "@gmail.com"
