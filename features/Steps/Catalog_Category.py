from behave import *

from Pages.Catalog_Category_Page_Object import Catalog_Category

# @step("I should see Export to XML")
# def i_should_see_export_to_xml(context):
#     a = Catalog_Category(context.driver)
#     a.i_should_see_export_to_xml()
#
#
# @step("I should see Export to Excel")
# def i_should_see_export_to_excel(context):
#     a = Catalog_Category(context.driver)
#     a.i_should_see_export_to_excel()
#
#
# @step('I should able to select import file path "{}"')
# def i_should_able_to_select_import_file(context, path):
#     a = Catalog_Category(context.driver)
#     a.i_should_able_to_select_import_file(path)
#
#
# @step('I should able to click button of "{}"')
# def i_should_able_to_click_button_of_Import_from_excel(context, value):
#     a = Catalog_Category(context.driver)
#     a.i_should_able_to_click_button_of_Import_from_excel(value)
#
#
# @step('I should see message of "{}" POP UP')
# def i_should_able_to_see_error_message_of_Import(context, childitem):
#     a = Catalog_Category(context.driver)
#     a.i_should_able_to_see_error_message_of_Import(childitem)
#
#
# @step('I should able to enter category name {} in search')
# def i_should_able_to_enter_category_name(context, name):
#     a = Catalog_Category(context.driver)
#     a.i_should_able_to_enter_category_name_in_Search(name)
#
#
# @step('I should see Published field and select value "{}"')
# def i_should_see_published_field_and_select_value(context, publish):
#     a = Catalog_Category(context.driver)
#     a.i_should_see_published_field_and_select_value(publish)
#
#
# @step("I see search result by Published field and count number of items")
# def i_see_search_result(context):
#     a = Catalog_Category(context.driver)
#     a.i_see_search_result()
#
#
# @step("I should able to click on Export to XML {}")
# def i_should_click_on_Export_to_XML(context, export):
#     a = Catalog_Category(context.driver)
#     a.i_should_click_on_Export_to_XML(export)
#
#
# @step("I should see downloaded file")
# def i_should_verify_download_file(context):
#     a = Catalog_Category(context.driver)
#     a.i_should_verify_download_file()
#
#
# @step("I should see see category table")
# def i_should_see_category_table(context):
#     a = Catalog_Category(context.driver)
#     a.i_should_see_category_table()
#
#
# @step('I should edit "{}" details by click "{}" under category')
# def i_should_edit_by_category(context, categoryfullname, clickedit):
#     a = Catalog_Category(context.driver)
#     a.i_should_edit_by_category(categoryfullname, clickedit)
#
#
# @step("I should see saved successfully message on category")
# def i_should_see_saved_successfully_message_on_categories(context):
#     s = Catalog_Category(context.driver)
#     s.verify_success_save_category()
#
#
# @step("I should able to click save {} Button")
# def i_should_able_to_click_save(context, btn):
#     s = Catalog_Category(context.driver)
#     s.i_should_able_to_click_save(btn)
#
#
# @step("I should able to enter category name as {}")
# def i_should_able_to_enter_category_name_as(context, field):
#     s = Catalog_Category(context.driver)
#     s.i_should_able_to_enter_category_name_as(field)
#
#
# @step("I should able to select Parent category as {}")
# def select_parent_category_as(context, parent):
#     s = Catalog_Category(context.driver)
#     s.i_should_able_to_select_parent_category_as(parent)
#
#
# @step("I should able to see and click on checkbox of {} by id {}")
# def category_checkbox(context, checkbox, value):
#     s = Catalog_Category(context.driver)
#     s.i_should_able_to_select_checkbox_under_category(checkbox, value)
#
#
# @Step('Verify user must be able to see "{}" Button on Categories Page')
# def step_impl(context, value):
#     Import_buttons = Catalog_Category(context.driver)
#     Import_buttons.user_should_able_to_click_Export_Button_expand(value)
#
#
# # @step('Verify user must be able to click on "{}" Button')
# # def step_impl(context, value):
# #     click_buttons = Catalog_Category(context.driver)
# #     click_buttons.user_should_able_to_click_Exportoptions_Button_expand(value)
#
#
# # @Step('Verify user must be able to check downloaded Export file from "{}"')
# # def step_impl(context, path):
# #     Import_buttons = Catalog_Category(context.driver)
# #     Import_buttons.Verify_downloaded_file(path)
#
#
# # @Step('Click checkbox of "show on home page"')
# # def step_impl(context):
# #     click_checkbox = Catalog_Category(context.driver)
# #     click_checkbox.click_Show_on_home_page_checkbox()
#
#
# # @Step('Click checkbox of "Allow customers to select page size"')
# # def step_impl(context):
# #     click_checkbox = Catalog_Category(context.driver)
# #     click_checkbox.allow_customers_to_select_page_size()
#
#
# # @step('Verify user must be able to see "{}" choose file POP UP window')
# # def step_impl(context, value):
# #     see_popup = Catalog_Category(context.driver)
# #     see_popup.user_should_able_to_see_import_popup(value)
#
#
# @step('I set display order "{}"')
# def step_impl(context, order):
#     see_order = Catalog_Category(context.driver)
#     see_order.i_set_display_order(order)
#
#
# @step('Verify user must be able to select Import file path "{}"')
# def step_impl(context, path):
#     click_choose = Catalog_Category(context.driver)
#     click_choose.user_should_able_to_select_import_file(path)
#
#
# @step('Verify user must be able to select Picture file "{}"')
# def step_impl(context, path):
#     click_choose = Catalog_Category(context.driver)
#     click_choose.user_should_able_to_select_picture_file(path)
#
#
# @step('Verify user must be able to click button of "{}"')
# def step_impl(context, value):
#     click_importbutton = Catalog_Category(context.driver)
#     click_importbutton.user_should_able_to_click_button_of_Import(value)
#
#
# @step('Verify user must be able to see the Error Message of "{}" POP UP')
# def step_impl(context, childitem):
#     error_message = Catalog_Category(context.driver)
#     error_message.user_should_able_to_see_error_message_of_Import(childitem)
#
#
# @step('I select parent category "{}"')
# def step_impl(context, first):
#     prnt_ctg = Catalog_Category(context.driver)
#     prnt_ctg.select_parent_categories(first)
#
#
# @step('Verify user must be able to go on "{}" from "{}"')
# def step_impl(context, childitem, parentitem):
#     select_item = Catalog_Category(context.driver)
#     select_item.go_to_childitem_page(childitem, parentitem)
#
#
# @Step('Verify user must be able to see "{}" Button')
# def step_impl(context, value):
#     Delete_buttons = Catalog_Category(context.driver)
#     Delete_buttons.user_should_able_to_see_Delete_Button(value)
#
#
# @step('Verify user must be able to click "{}" Button')
# def step_impl(context, value):
#     click_delete = Catalog_Category(context.driver)
#     click_delete.user_should_able_to_click_Delete_Button(value)
#
#
# @step('Verify user must be able to click "{}" Button by name')
# def step_impl(context, value):
#     click_delete = Catalog_Category(context.driver)
#     click_delete.user_should_able_to_delete_selected_Delete_Button(value)
#
#
# @step("Verify user must be able to click YES on Delete POPUP")
# def step_impl(context):
#     POPUP_delete = Catalog_Category(context.driver)
#     POPUP_delete.user_should_able_to_click_YES_delete_popup()
#
#
# @step('Verify user must be able to select "{}" checkbox to Delete')
# def step_impl(context, fullname):
#     delete_byname = Catalog_Category(context.driver)
#     delete_byname.select_deletecheckbox_by_name(fullname)
#
#
# @step('I see search result by Published Only and Verify')
# def step_impl(context):
#     Publish = Catalog_Category(context.driver)
#     Publish.search_result_by_Published_Only_and_Verify()

# CREATED BY ADITYA
@step('Verify user must be able to click on "{}" Button')
def step_impl(context, value):
    click_buttons = Catalog_Category(context.driver)
    click_buttons.user_should_able_to_click_Button(value)

# CREATED BY ADITYA
@step('Verify user must be able to click on drop down options button and select "{}"')
def step_impl(context, value):
    click_options = Catalog_Category(context.driver)
    click_options.user_should_able_to_click_Exportoptions_Button_expand(value)

# CREATED BY ADITYA
@Step('Verify user must be able to check downloaded Export file from "{}"')
def step_impl(context, path):
    Import_buttons = Catalog_Category(context.driver)
    Import_buttons.Verify_downloaded_file(path)

# CREATED BY ADITYA
@Step('Click checkbox of "show on home page"')
def step_impl(context):
    click_cbox = Catalog_Category(context.driver)
    click_cbox.click_Show_on_home_page_checkbox()

# CREATED BY ADITYA
@Step('Click checkbox of "Allow customers to select page size"')
def step_impl(context):
    click_checkbox = Catalog_Category(context.driver)
    click_checkbox.allow_customers_to_select_page_size()

# CREATED BY ADITYA
@step('Verify user must be able to see "{}" choose file POP UP window')
def step_impl(context, value):
    see_popup = Catalog_Category(context.driver)
    see_popup.user_should_able_to_see_import_popup(value)

# CREATED BY ADITYA
@step('I set display order "{}"')
def step_impl(context, order):
    see_order = Catalog_Category(context.driver)
    see_order.i_set_display_order(order)

# CREATED BY ADITYA
@step('Verify user must be able to select Import file path "{}"')
def step_impl(context, path):
    click_choose = Catalog_Category(context.driver)
    click_choose.user_should_able_to_select_import_file(path)

# CREATED BY ADITYA
@step('Verify user must be able to select Picture file "{}"')
def step_impl(context, path):
    click_choose = Catalog_Category(context.driver)
    click_choose.user_should_able_to_select_picture_file(path)

# CREATED BY ADITYA
@step('Verify user must be able to click button of "{}"')
def step_impl(context, value):
    click_importbutton = Catalog_Category(context.driver)
    click_importbutton.user_should_able_to_click_button_of_Import(value)

# CREATED BY ADITYA
@step('Verify user must be able to see the Error Message of "{}" POP UP')
def step_impl(context, childitem):
    error_message = Catalog_Category(context.driver)
    error_message.user_should_able_to_see_error_message_of_Import(childitem)

# CREATED BY ADITYA
@step('I select parent category "{}"')
def step_impl(context, first):
    prnt_ctg = Catalog_Category(context.driver)
    prnt_ctg.select_parent_categories(first)

# CREATED BY ADITYA
@step('Verify user must be able to go on "{}" from "{}"')
def step_impl(context, childitem, parentitem):
    select_item = Catalog_Category(context.driver)
    select_item.go_to_childitem_page(childitem, parentitem)

# CREATED BY ADITYA
@Step('Verify user must be able to see "{}" Button')
def step_impl(context, value):
    Delete_buttons = Catalog_Category(context.driver)
    Delete_buttons.user_should_able_to_see_Button(value)

# CREATED BY ADITYA
@step('Verify user must be able to click "{}" Button')
def step_impl(context, value):
    click_delete = Catalog_Category(context.driver)
    click_delete.user_should_able_to_click_Delete_Button(value)

# CREATED BY ADITYA
@step('Verify user must be able to click "{}" Button by name')
def step_impl(context, value):
    click_delete = Catalog_Category(context.driver)
    click_delete.user_should_able_to_delete_selected_Delete_Button(value)

# CREATED BY ADITYA
@step("Verify user must be able to click YES on Delete POPUP")
def step_impl(context):
    POPUP_delete = Catalog_Category(context.driver)
    POPUP_delete.user_should_able_to_click_YES_delete_popup()

# CREATED BY ADITYA
@step('Verify user must be able to select "{}" checkbox to Delete')
def step_impl(context, fullname):
    delete_byname = Catalog_Category(context.driver)
    delete_byname.select_deletecheckbox_by_name(fullname)

# CREATED BY ADITYA
@step('I see search result by Published Only and Verify')
def step_impl(context):
    Publish = Catalog_Category(context.driver)
    Publish.search_result_by_Published_Only_and_Verify()

# CREATED BY ADITYA
@step('I set description "{}"')
def i_set_full_description(context, descp):
    btn = Catalog_Category(context.driver)
    btn.i_set_description(descp)


# CREATED BY RUPALI
@step("I should see Export to XML")
def i_should_see_export_to_xml(context):
    a = Catalog_Category(context.driver)
    a.i_should_see_export_to_xml()


# CREATED BY RUPALI
@step("I should see Export to Excel")
def i_should_see_export_to_excel(context):
    a = Catalog_Category(context.driver)
    a.i_should_see_export_to_excel()


# CREATED BY RUPALI
@step('I should able to select import file path "{}"')
def i_should_able_to_select_import_file(context, path):
    a = Catalog_Category(context.driver)
    a.i_should_able_to_select_import_file(path)


# CREATED BY RUPALI
@step('I should able to click button of "{}"')
def i_should_able_to_click_button_of_Import_from_excel(context, value):
    a = Catalog_Category(context.driver)
    a.i_should_able_to_click_button_of_Import_from_excel(value)


# CREATED BY RUPALI
@step('I should see message of "{}" POP UP')
def i_should_able_to_see_error_message_of_Import(context, childitem):
    a = Catalog_Category(context.driver)
    a.i_should_able_to_see_error_message_of_Import(childitem)


# CREATED BY RUPALI
@step('I should able to enter category name {} in search')
def i_should_able_to_enter_category_name(context, name):
    a = Catalog_Category(context.driver)
    a.i_should_able_to_enter_category_name_in_Search(name)


# CREATED BY RUPALI
@step('I should see Published field and select value "{}"')
def i_should_see_published_field_and_select_value(context, publish):
    a = Catalog_Category(context.driver)
    a.i_should_see_published_field_and_select_value(publish)


# CREATED BY RUPALI
@step("I see search result by Published field and count number of items")
def i_see_search_result(context):
    a = Catalog_Category(context.driver)
    a.i_see_search_result()


# CREATED BY RUPALI
@step("I should able to click on Export to XML {}")
def i_should_click_on_Export_to_XML(context, export):
    a = Catalog_Category(context.driver)
    a.i_should_click_on_Export_to_XML(export)


# CREATED BY RUPALI
@step("I should see downloaded file")
def i_should_verify_download_file(context):
    a = Catalog_Category(context.driver)
    a.i_should_verify_download_file()


# CREATED BY RUPALI
@step("I should see see category table")
def i_should_see_category_table(context):
    a = Catalog_Category(context.driver)
    a.i_should_see_category_table()


# CREATED BY RUPALI
@step('I should edit "{}" details by click "{}" under category')
def i_should_edit_by_category(context, categoryfullname, clickedit):
    a = Catalog_Category(context.driver)
    a.i_should_edit_by_category(categoryfullname, clickedit)


# CREATED BY RUPALI
@step("I should see saved successfully message on category")
def i_should_see_saved_successfully_message_on_categories(context):
    s = Catalog_Category(context.driver)
    s.verify_success_save_category()


# CREATED BY RUPALI
@step("I should able to click save {} Button")
def i_should_able_to_click_save(context, btn):
    s = Catalog_Category(context.driver)
    s.i_should_able_to_click_save(btn)


# CREATED BY RUPALI
@step("I should able to enter category name as {}")
def i_should_able_to_enter_category_name_as(context, field):
    s = Catalog_Category(context.driver)
    s.i_should_able_to_enter_category_name_as(field)


# CREATED BY RUPALI
@step("I should able to select Parent category as {}")
def select_parent_category_as(context, parent):
    s = Catalog_Category(context.driver)
    s.i_should_able_to_select_parent_category_as(parent)


# CREATED BY RUPALI
@step("I should able to see and click on checkbox of {} by id {}")
def category_checkbox(context, checkbox, value):
    s = Catalog_Category(context.driver)
    s.i_should_able_to_select_checkbox_under_category(checkbox, value)
