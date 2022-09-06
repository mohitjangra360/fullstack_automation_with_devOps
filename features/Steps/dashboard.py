from behave import *

from Pages.Login.LoginPage import LoginPage
from Utilities.readProperty import ReadConfig

username = ReadConfig.getUserName()

@when("Enter User Name")
def step_impl(context):
    av = LoginPage(context.driver)
    av.setUsername(username)
