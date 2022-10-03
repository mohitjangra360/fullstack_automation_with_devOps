import os
import time

import PyPDF2
from selenium import webdriver
from selenium.webdriver.common.by import By

class LoginDemoPage:

    # op = webdriver.ChromeOptions()
    # op.add_experimental_option("prefs",{"download.default_directory" : "D:\\nopCommerce\\Down"})
    # driver = webdriver.Chrome(executable_path='D:/data/ChromeDriverpath/chromedriver.exe', options=op)
    username_by_id = "Email"
    password_by_name = "Password"
    login_link_by_xpath = "//div[@class='header-links']//a[text()='Log in']"
    login_btn_by_xpath = "//div[@class='returning-wrapper']//div//input[@value='Log in']"

    def __init__(self, driver):
        self.driver = driver

    def clickOnLogin_link(self):
        self.driver.find_element(By.XPATH, self.login_link_by_xpath).click()
        time.sleep(3)

    def setDemoUsername(self, username):
        self.driver.find_element(By.ID, self.username_by_id).clear()
        self.driver.find_element(By.ID, self.username_by_id).send_keys(username)

    def setDemoPassword(self, password):
        self.driver.find_element(By.NAME, self.password_by_name).clear()
        self.driver.find_element(By.NAME, self.password_by_name).send_keys(password)

    def clickOnLogin_btn(self):
        self.driver.find_element(By.XPATH, self.login_btn_by_xpath).click()
        time.sleep(3)

    def verify_product_on_home_page(self, Product_Name, btn, Product_Title):
        products = "//div[@class='product-grid home-page-product-grid']//h2[@class='product-title']//a"
        get_products = self.driver.find_elements(By.XPATH, f"{products}")
        products_value = []

        for get in get_products:
            name = get.text
            products_value.append(name)

        if Product_Name in products_value:
            Add_cart = f"//div[@class='product-grid home-page-product-grid']//h2[contains(., '{Product_Name}')]//..//*[@value='{btn}']"
            self.driver.find_element(By.XPATH, Add_cart).click()
            time.sleep(2)
            actual_product_title = self.driver.title
            expected_title = Product_Title
            if actual_product_title == expected_title:
                add_to_cart = f"//div[@class='overview']//input[@value='{btn}']"
                self.driver.find_element(By.XPATH, f"{add_to_cart}").click()
                time.sleep(2)

                Success_Message = "The product has been added to your shopping cart"
                get_message = self.driver.find_element(By.XPATH, "//p[@class='content']")
                message = get_message.get_attribute("textContent")

                if message == Success_Message:
                    time.sleep(2)
                    self.driver.find_element(By.XPATH, "//p[@class='content']//a[contains(text(), 'shopping cart')]").click()
                    time.sleep(2)
                else:
                    assert False
            else:
                print("detail page not open, it directly go in cart")
                time.sleep(1)
                self.driver.find_element(By.XPATH, "//p[@class='content']//a[contains(text(), 'shopping cart')]").click()
                time.sleep(2)
        else:
            assert False

    def click_and_verify_product_on_cart_page(self, btn, Product_Name):
        tablevalue = "//table[@class='cart']//tbody//tr//td[3]//a"
        get_tablevalue = self.driver.find_elements(By.XPATH, f"{tablevalue}")
        values_list = []
        for v in get_tablevalue:
            productname = v.text
            values_list.append(productname)
            print(values_list)
        if Product_Name in values_list:
            assert True
        else:
            assert False

    def click_checkout_and_confirm_order(self, chkout, Checkout_Title):
        self.driver.find_element(By.XPATH, "//div[@class='terms-of-service']//input[@type='checkbox']").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, f"//button[contains(text(),'{chkout}')]").click()
        time.sleep(2)

        actual_checkout_title = self.driver.title
        expected_title = Checkout_Title
        if actual_checkout_title == expected_title:
            chk = "//div[@class='step-title']//h2"
            Continue = "//li[@class='tab-section allow active']//*[@value='Continue']"
            Confirm = "//li[@class='tab-section allow active']//*[@value='Confirm']"
            getchk_value = self.driver.find_elements(By.XPATH, f"{chk}")
            Checkout_list = []
            for value in getchk_value:
                chck_name = value.get_attribute("textContent")
                Checkout_list.append(chck_name)
                if "Billing address" == chck_name:
                    self.driver.find_element(By.XPATH, f"{Continue}").click()
                    time.sleep(2)
                elif "Shipping address" == chck_name:
                    self.driver.find_element(By.XPATH, f"{Continue}").click()
                    time.sleep(2)
                elif "Shipping method" == chck_name:
                    self.driver.find_element(By.XPATH, f"{Continue}").click()
                    time.sleep(2)
                elif "Payment method" == chck_name:
                    self.driver.find_element(By.XPATH, f"{Continue}").click()
                    time.sleep(2)
                elif "Payment information" == chck_name:
                    self.driver.find_element(By.XPATH, f"{Continue}").click()
                    time.sleep(2)
                elif "Confirm order" == chck_name:
                    self.driver.find_element(By.XPATH, f"{Confirm}").click()
                    time.sleep(2)
        else:
            assert False

        Suceess_title = "Your order has been successfully processed!"
        if Suceess_title in self.driver.page_source:
            self.driver.find_element(By.XPATH, "//div[@class='page-body checkout-data']//*[@value='Continue']").click()
        else:
            assert False

    def Go_to_and_verify_ordered_product_detail(self, value, Product_Name):
        My_Account = "//div[@class='column my-account']//ul//li//a"
        My_Account_values = self.driver.find_elements(By.XPATH, f"{My_Account}")
        Text = []
        for words in My_Account_values:
            get_text = words.text
            Text.append(get_text)
        if value in Text:
            self.driver.find_element(By.XPATH,
                                     f"//div[@class='column my-account']//ul//li//a[contains(text(),'{value}')]").click()
            time.sleep(2)
            Page_header = self.driver.find_element(By.XPATH, f"//h1[text() ='My account - Orders']").is_displayed()
            if Page_header:
                Detail_buttons = "//div[@class='page account-page order-list-page']//strong"
                get_title = self.driver.find_elements(By.XPATH, f"{Detail_buttons}")
                order_numbers = []
                for v in get_title:
                    get_value = v.text
                    order_numbers.append(get_value)
                for i in range(1, len(order_numbers)):
                    Page_header01 = self.driver.find_element(By.XPATH, f"//h1[text() ='My account - Orders']").is_displayed()
                    if Page_header01:
                        by_Order = f"//div[@class='section order-item']//child::div//strong[contains(text(), '{order_numbers[i]}')]//..//following-sibling::div//input[@value='Details']"
                        self.driver.find_element(By.XPATH, f"{by_Order}").click()
                        time.sleep(2)
                        if Product_Name in self.driver.page_source:
                            try:
                                time.sleep(3)
                                print("product found in orders")
                                break
                            except Exception:
                                self.driver.back()
                        break
        else:
            assert False

    def Click_download_invoice_and_verify_product_details(self, Product_Name):
        getorder_number = self.driver.find_element(By.XPATH, "//div[@class='order-number']//strong")
        order_number = getorder_number.text
        order,value = order_number.split("#")
        self.driver.find_element(By.XPATH, "//div[@class='page-title']//a[text()='PDF Invoice']").click()
        time.sleep(2)
        while not os.path.exists(r'C:\Users\User\Downloads'):
            time.sleep(2)
        if os.path.isfile(fr'C:\Users\User\Downloads\order_{value}.pdf'):
            pdfFileObj = open(fr'C:\Users\User\Downloads\order_{value}.pdf', 'rb')
            pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
            print(pdfReader.numPages)
            pageObj = pdfReader.getPage(0)
            get_filetext = pageObj.extractText()
            print(pageObj.extractText())
            if Product_Name in get_filetext:
                assert True
            else:
                assert False
            pdfFileObj.close()
        else:
            print("File download is not completed")

