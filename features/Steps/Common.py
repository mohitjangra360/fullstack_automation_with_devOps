import time

from behave import *
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from Pages.Common_Method import CommonMethod
from Pages.LoginPage import LoginPage
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


@step("I am On Login Page")
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


@step('I should see "{}"')
def i_should_see(context, value):
    text = CommonMethod(context.driver)
    text.i_should_see(value)


@step('I should see "{}" input field by {}')
def i_should_see_input_field(context, value, locator):
    input = CommonMethod(context.driver)
    input.i_should_see_input_field(value, locator)


@step('I Select "{}" from "{}"')
def step_impl(context, childitem, parentitem):
    select_item = CommonMethod(context.driver)
    select_item.i_select_child_from_parent_side_menu_bar(childitem, parentitem)


@step("I goto {X} >> {Y} >> {Z}")
def i_goto(context, X, Y, Z):
    v = CommonMethod(context.driver)
    v.i_goto(X, Y, Z)


@step("I wait {} seconds")
def step_impl(context, wait):
    time.sleep(int(wait))


@step('I should see "{}" select field by {}')
def i_should_see_select_field(context, value, locator):
    input = CommonMethod(context.driver)
    input.i_should_see_select_field(value, locator)

@step('I should see search "{}" select field by "{}"')
def i_should_see_select_field_in_search(context, value, locator):
    input_bysearch = CommonMethod(context.driver)
    input_bysearch.i_should_see_select_field_in_search(value, locator)


@step('I should click "{}" select field by "{}" and select "{}"')
def i_should_click_selectfield(context, value, locator, select):
    input = CommonMethod(context.driver)
    input.i_should_click_select_field(value, locator, select)


@step('I should click "{}"')
def i_should_click_search_field(context, button):
    butn = CommonMethod(context.driver)
    butn.i_click_search(button)
