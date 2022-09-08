from behave import *

from Pages.LoginPage import LoginPage


@step('I set field value "{}" and "{}"')
def step_impl(context, username, password):
    """
    :type context: behave.runner.Context
    :type username: str
    :type password: str
    """
    login = LoginPage(context.driver)
    login.setUsername(username)
    login.setPassword(password)
    login.clickOnLogin()
