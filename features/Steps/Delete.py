from behave import *

from Pages.Product.DeletePage import Delete
from Pages.Product.ImportPage import Import


@step('Verify user must be able to go on "{}" from "{}"')
def step_impl(context, childitem, parentitem):
    select_item = Delete(context.driver)
    select_item.go_to_product_page(childitem, parentitem)

@Step('Verify user must be able to see "{}" Button')
def step_impl(context, value):
    Delete_buttons = Delete(context.driver)
    Delete_buttons.user_should_able_to_see_Import_Button(value)

