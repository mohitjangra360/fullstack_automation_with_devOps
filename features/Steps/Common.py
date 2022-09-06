from behave import *
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from Utilities.CustomLogger import LogGen
from Utilities.readProperty import ReadConfig

baseUrl = ReadConfig.getApplicationURL()
mylog = LogGen.loggen()


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


@step("User On Login Page")
def user_on_login_page(context):
    global logopage
    actual_title = context.driver.title
    expected_title = "Your store. Login"
    if actual_title == expected_title:
        assert True
    else:
        assert False
