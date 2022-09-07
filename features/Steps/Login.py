from behave import *

from Pages.Common_Method.CommonMathod import CommonMethod
from Pages.Login.LoginPage import LoginPage


@step('I set field value "{username}" and "{password}"')
def step_impl(context, username, password):
    """
    :type context: behave.runner.Context
    :type username: str
    :type password: str
    """
    v = LoginPage(context.driver)
    v.setUsername(username)
    v.setPassword(password)
