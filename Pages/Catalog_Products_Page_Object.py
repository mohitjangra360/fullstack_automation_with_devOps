import random
import string
import time

from selenium.webdriver.common.by import By


class Catalog_Product:

    def __init__(self, driver):
        self.driver = driver

    def i_see_add_new_btn(self):
        self.driver.find_element(By.XPATH, "//*[contains(@href,'Create')]").is_displayed()

    def click_on_add_new_cust_btn(self):
        self.driver.find_element(By.XPATH, "//*[contains(@href,'Create')]").click()

    def i_see_download_catalog_pdf_btn(self):
        self.driver.find_element(By.XPATH, "//button[@name='download-catalog-pdf']").is_displayed()

    def i_click_on_download_catalog_btn(self):
        self.driver.find_element(By.XPATH, "//button[@name='download-catalog-pdf']").click()

    def i_see_export_btn(self):
        self.driver.find_element(By.XPATH, "//button[@class='btn btn-success']").is_displayed()

    def i_click_on_export_btn(self):
        self.driver.find_element(By.XPATH, "//button[@data-toggle='dropdown']").click()

    def i_see_export_to_xml_all(self):
        self.driver.find_element(By.XPATH, "//button[@name='exportxml-all']").is_displayed()

    def i_see_export_to_xml_selected(self):
        self.driver.find_element(By.XPATH, "//button[@id='exportxml-selected']").is_displayed()

    def i_see_export_to_excel_all(self):
        self.driver.find_element(By.XPATH, "//button[@name='exportexcel-all']").is_displayed()

    def i_see_export_to_excel_selected(self):
        self.driver.find_element(By.XPATH, "//button[@name='exportexcel-all']").is_displayed()

    def i_see_import(self):
        self.driver.find_element(By.XPATH, "//button[@name='importexcel']").is_displayed()

    def i_click_on_import(self):
        self.driver.find_element(By.XPATH, "//button[@name='importexcel']").click()

    def i_see_choose_file_popup_box(self):
        self.driver.find_element(By.XPATH, "//input[@id='importexcelfile']").is_displayed()

    def i_see_delete_btn(self):
        self.driver.find_element(By.XPATH, "//button[@id='delete-selected']").is_displayed()

    def i_click_on_delete_btn(self):
        self.driver.find_element(By.XPATH, "//button[@id='delete-selected']").click()

    def i_set_products_name(self, product_name):
        self.driver.find_element(By.XPATH, "//input[@id='Name']").send_keys(product_name)

    def i_set_short_description(self, short_descp):
        self.driver.find_element(By.XPATH, "//textarea[@id='ShortDescription']").send_keys(short_descp)

    def i_set_full_description(self, full_descp):
        self.driver.find_element(By.XPATH, "//textarea[@id='FullDescription']").send_keys(full_descp)


    def set_mail_for_cust(self):
        self.driver.find_element(By.XPATH, "//input[@id='Email']").send_keys(self.random_email() + "@gmail.com")

    def random_email(size = 10, char=string.ascii_lowercase + string.digits):
        return ''.join(random.choice(char) for x in range(size))

    def set_password(self, password):
        self.driver.find_element(By.XPATH, "//input[@id='Password']").send_keys(password)

    def set_firstname(self, firstname):
        self.driver.find_element(By.XPATH, "//input[@id='FirstName']").send_keys(firstname)

    def set_lastname(self, lastname):
        self.driver.find_element(By.XPATH, "//input[@id='LastName']").send_keys(lastname)

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






