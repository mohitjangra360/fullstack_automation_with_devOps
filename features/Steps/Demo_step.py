import time

from behave import *
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from Pages.Demo_Page import LoginDemoPage
from Utilities.CustomLogger import LogGen
from Utilities.readProperty import ReadConfig


basedemoUrl = ReadConfig.getDemoApplicationURL()
mylog = LogGen.loggen()
username = ReadConfig.getDemoUserName()
password = ReadConfig.getDemoPassword()
Recipient_Name = ReadConfig.getRecipientName()
Recipient_Email = ReadConfig.getRecipientEmail()
Product_Title = ReadConfig.getproducttitle()
Product_Name = ReadConfig.getproductname()
Checkout_Title = ReadConfig.getcheckouttitle()


@step("Open Demo Browser")
def launch_browser(context):
    context.driver = webdriver.Chrome(ChromeDriverManager().install())
    context.driver.maximize_window()
    mylog.info("Open Browser")
    context.driver.get(basedemoUrl)


@step("I click on Log In")
def click_login(context):
    login_link = LoginDemoPage(context.driver)
    mylog.info('Close Browser')
    login_link.clickOnLogin_link()


@step("I am On Demo Login Page")
def user_on_login_page(context):
    global logopage
    actual_title = context.driver.title
    expected_title = "Demo Web Shop. Login"
    if actual_title == expected_title:
        assert True
    else:
        assert False


@step("I login as Demo admin")
def user_login_as_admin(context):
    common_method = LoginDemoPage(context.driver)
    common_method.setDemoUsername(username)
    common_method.setDemoPassword(password)
    common_method.clickOnLogin_btn()


@step('I verify product visible on home page and click "{}"')
def verify_product_on_home_page(context, btn):
    product_visble = LoginDemoPage(context.driver)
    product_visble.verify_product_on_home_page(Product_Name, btn, Product_Title)


@step('I click on "{}" and verify product in cart')
def verify_product_on_cart_page(context, btn):
    click_btn = LoginDemoPage(context.driver)
    click_btn.click_and_verify_product_on_cart_page(btn, Product_Name)


@step('I click on "{}" and confirm order')
def verify_product_confirm_order(context, chkout):
    click_btn = LoginDemoPage(context.driver)
    click_btn.click_checkout_and_confirm_order(chkout, Checkout_Title)


@step('Go to "{}" and verify ordered product detail')
def verify_order_details_with_product(context, value):
    click_btn = LoginDemoPage(context.driver)
    click_btn.Go_to_and_verify_ordered_product_detail(value, Product_Name)


@step('Click download invoice and verify product details')
def download_verify_file(context):
    click_btn = LoginDemoPage(context.driver)
    click_btn.Click_download_invoice_and_verify_product_details(Product_Name)
