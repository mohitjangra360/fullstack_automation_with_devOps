from behave import *

from Pages.Product.ImportPage import Import


@step('Verify user must be able to go on "{}" from "{}" product page')
def step_impl(context, childitem, parentitem):
    select_item = Import(context.driver)
    select_item.go_to_childitem_page(childitem, parentitem)

@Step('Verify user must be able to see "{}" Button on Product Page')
def step_impl(context, value):
    Import_buttons = Import(context.driver)
    Import_buttons.user_should_able_to_see_Import_Button(value)

@step('Verify user must be able to click on "{}" Button')
def step_impl(context, value):
    click_buttons = Import(context.driver)
    click_buttons.user_should_able_to_click_Import_Button(value)

@step('Verify user must be able to see "{}" choose file POP UP window')
def step_impl(context, value):
    see_popup = Import(context.driver)
    see_popup.user_should_able_to_see_import_popup(value)

@step('Verify user must be able to select Import file path "{}"')
def step_impl(context,path):
    click_choose = Import(context.driver)
    click_choose.user_should_able_to_select_import_file(path)

@step('Verify user must be able to click button of "{}"')
def step_impl(context, value):
    click_importbutton = Import(context.driver)
    click_importbutton.user_should_able_to_click_button_of_Import(value)

@step('Verify user must be able to see the Error Message of "{}" POP UP')
def step_impl(context, childitem):
    error_message = Import(context.driver)
    error_message.user_should_able_to_see_error_message_of_Import(childitem)