from behave import *

from Pages.Catalog_Category_Page_Object import Catalog_Category

@step('Verify user must be able to click on "{}" Button')
def step_impl(context, value):
    click_buttons = Catalog_Category(context.driver)
    click_buttons.user_should_able_to_click_Button(value)

@step('Verify user must be able to click on drop down options button and select "{}"')
def step_impl(context, value):
    click_options = Catalog_Category(context.driver)
    click_options.user_should_able_to_click_Exportoptions_Button_expand(value)

@Step('Verify user must be able to check downloaded Export file from "{}"')
def step_impl(context, path):
    Import_buttons = Catalog_Category(context.driver)
    Import_buttons.Verify_downloaded_file(path)

@Step('Click checkbox of "show on home page"')
def step_impl(context):
    click_cbox = Catalog_Category(context.driver)
    click_cbox.click_Show_on_home_page_checkbox()

@Step('Click checkbox of "Allow customers to select page size"')
def step_impl(context):
    click_checkbox = Catalog_Category(context.driver)
    click_checkbox.allow_customers_to_select_page_size()

@step('Verify user must be able to see "{}" choose file POP UP window')
def step_impl(context, value):
    see_popup = Catalog_Category(context.driver)
    see_popup.user_should_able_to_see_import_popup(value)

@step('I set display order "{}"')
def step_impl(context, order):
    see_order = Catalog_Category(context.driver)
    see_order.i_set_display_order(order)

@step('Verify user must be able to select Import file path "{}"')
def step_impl(context,path):
    click_choose = Catalog_Category(context.driver)
    click_choose.user_should_able_to_select_import_file(path)

@step('Verify user must be able to select Picture file "{}"')
def step_impl(context, path):
    click_choose = Catalog_Category(context.driver)
    click_choose.user_should_able_to_select_picture_file(path)

@step('Verify user must be able to click button of "{}"')
def step_impl(context, value):
    click_importbutton = Catalog_Category(context.driver)
    click_importbutton.user_should_able_to_click_button_of_Import(value)

@step('Verify user must be able to see the Error Message of "{}" POP UP')
def step_impl(context, childitem):
    error_message = Catalog_Category(context.driver)
    error_message.user_should_able_to_see_error_message_of_Import(childitem)

@step('I select parent category "{}"')
def step_impl(context, first):
    prnt_ctg = Catalog_Category(context.driver)
    prnt_ctg.select_parent_categories(first)

@step('Verify user must be able to go on "{}" from "{}"')
def step_impl(context, childitem, parentitem):
    select_item = Catalog_Category(context.driver)
    select_item.go_to_childitem_page(childitem, parentitem)

@Step('Verify user must be able to see "{}" Button')
def step_impl(context, value):
    Delete_buttons = Catalog_Category(context.driver)
    Delete_buttons.user_should_able_to_see_Button(value)

@step('Verify user must be able to click "{}" Button')
def step_impl(context, value):
    click_delete = Catalog_Category(context.driver)
    click_delete.user_should_able_to_click_Delete_Button(value)

@step('Verify user must be able to click "{}" Button by name')
def step_impl(context, value):
    click_delete = Catalog_Category(context.driver)
    click_delete.user_should_able_to_delete_selected_Delete_Button(value)

@step("Verify user must be able to click YES on Delete POPUP")
def step_impl(context):
    POPUP_delete = Catalog_Category(context.driver)
    POPUP_delete.user_should_able_to_click_YES_delete_popup()

@step('Verify user must be able to select "{}" checkbox to Delete')
def step_impl(context, fullname):
    delete_byname = Catalog_Category(context.driver)
    delete_byname.select_deletecheckbox_by_name(fullname)

@step('I see search result by Published Only and Verify')
def step_impl(context):
    Publish = Catalog_Category(context.driver)
    Publish.search_result_by_Published_Only_and_Verify()




