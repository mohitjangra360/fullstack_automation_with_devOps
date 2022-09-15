from behave import *

from Pages.Product.ImportPage import Import


@step('Verify user must be able to go on "{}" from "{}" product page')
def step_impl(context, childitem, parentitem):
    select_item = Import(context.driver)
    select_item.go_to_product_page(childitem, parentitem)

@Step('Verify user must be able to see "{}" Button on Product Page')
def step_impl(context, value):
    Import_buttons = Import(context.driver)
    Import_buttons.user_should_able_to_see_Import_Button(value)

@step('Verify user must be able to click on "{}" Button')
def step_impl(context, value):
    click_buttons = Import(context.driver)
    click_buttons.user_should_able_to_click_Import_Button(value)

