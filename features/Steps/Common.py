import time

from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

from Pages.Common_Method.CommonMathod import CommonMethod
from Pages.Login.LoginPage import LoginPage
from Utilities.CustomLogger import LogGen
from Utilities.readProperty import ReadConfig

baseUrl = ReadConfig.getApplicationURL()
mylog = LogGen.loggen()
username = ReadConfig.getUserName()
password = ReadConfig.getPassword()


@step("Open Browser")
def launch_browser(context):
    context.driver = webdriver.Chrome(ChromeDriverManager().install())
    context.driver.maximize_window()
    mylog.info("Open Browser")
    context.driver.get(baseUrl)


@step("Close Browser")
def close_browser(context):
    mylog.info('Close Browser')
    context.driver.close()


@step("I am on Login Page")
def user_on_login_page(context):
    global logopage
    actual_title = context.driver.title
    expected_title = "Your store. Login"
    if actual_title == expected_title:
        assert True
    else:
        assert False


@step("I login as admin")
def user_login_as_admin(context):
    common_method = LoginPage(context.driver)
    common_method.setUsername(username)
    common_method.setPassword(password)
    common_method.clickOnLogin()


@step("I wait {} seconds")
def wait_on(context, wait_on):
    wait_time = int(wait_on)
    time.sleep(wait_time)


@step('I should see "{}"')
def i_should_see(context, textValue):
    v = CommonMethod(context.driver)
    v.i_should_see(textValue)


@step('I should see "{}" input field with {}')
def step_impl(context, val, locator):
    v = CommonMethod(context.driver)
    v.i_should_see_input_field(val, locator)


@step('I should see checkbox "{}" with {}')
def step_impl(context, value, locator):
    v = CommonMethod(context.driver)
    v.i_should_see_checkbox(value, locator)


@step('I should see button "{}" with {}')
def step_impl(context, value, locator):
    v = CommonMethod(context.driver)
    v.i_should_see_button(value, locator)



