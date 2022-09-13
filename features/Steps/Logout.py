from behave import *

from Pages.LogoutPage import LogoutPage


@step('I would see "Logout"')
def i_should_see_logout(context):
    output = LogoutPage(context.driver)
    output.logout_page_display()


@step("click on Logout button")
def logout_click(context):
    log = LogoutPage(context.driver)
    log.click_on_logout_button()
