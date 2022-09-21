from behave import *

from Pages.Product.DeletePage import Delete
from Pages.Product.ImportPage import Import


@step('Verify user must be able to go on "{}" from "{}"')
def step_impl(context, childitem, parentitem):
    select_item = Delete(context.driver)
    select_item.go_to_childitem_page(childitem, parentitem)

@Step('Verify user must be able to see "{}" Button')
def step_impl(context, value):
    Delete_buttons = Delete(context.driver)
    Delete_buttons.user_should_able_to_see_Delete_Button(value)

@step('Verify user must be able to click "{}" Button')
def step_impl(context, value):
    click_delete = Delete (context.driver)
    click_delete.user_should_able_to_click_Delete_Button(value)

@step("Verify user must be able to click YES on Delete POPUP")
def step_impl(context):
    POPUP_delete = Delete (context.driver)
    POPUP_delete.user_should_able_to_click_YES_delete_popup()