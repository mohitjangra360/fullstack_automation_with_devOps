from behave import *

from Pages.Common_Method import CommonMethod
from Pages.Dashboard.New_customer_page import NewCustomerPage


@step('I should see button "{}" with {}')
def step_impl(context, value, locator):
    btn = CommonMethod(context.driver)
    btn.i_should_see_expand_collapes_btn(value, locator)


@step("I should see new_customer expand button")
def step_impl(context):
    btn = NewCustomerPage(context.driver)
    btn.i_should_see_btn()
