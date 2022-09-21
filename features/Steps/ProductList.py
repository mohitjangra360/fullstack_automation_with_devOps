from behave import *

from Pages.ProductListPage import ProductListPage


@step("I should see columns in Product list")
def i_should_see_columns(context):
    see_columns = ProductListPage(context.driver)
    see_columns.i_should_see_product_column()


@step('I should able to change value "{}" of show items')
def i_should_select_items_to_display(context, value):
    a = ProductListPage(context.driver)
    a.i_should_select_items_to_display(value)


@step('I should able to verify value of show items selected "{}" and items display')
def i_verify_selected_items_and_displayed_items(context, valuee):
    b = ProductListPage(context.driver)
    b.i_verify_selected_items_and_displayed_items(valuee)


@step("I should able to click on edit btn of first product in list")
def i_should_able_to_click_on_edit_btn_of_frst_product(context):
    c = ProductListPage(context.driver)
    c.i_should_able_to_click_on_edit_btn_of_frst_product()


@step("I verify cards under advance mode")
def i_verify_cards_under_advance_mode(context):
    d = ProductListPage(context.driver)
    d.i_verify_cards_under_advance_mode()


@step('I edit the fields under card "{}"')
def i_edit_the_fields_under_product_info_card(context, card_name):
    e = ProductListPage(context.driver)
    e.i_edit_the_fields_under_product_info_card(card_name)


@step('I edit product name with "{}"')
def i_edit_the_product_name(context, edited_name):
    f = ProductListPage(context.driver)
    f.i_edit_the_product_name(edited_name)


@step('I edit Short description with "{}"')
def i_edit_the_Short_description(context, edited_name):
    g = ProductListPage(context.driver)
    g.i_edit_the_Short_description(edited_name)


@step('I edit Full description with "{}"')
def i_edit_the_Full_description(context, edited_name):
    h = ProductListPage(context.driver)
    h.i_edit_the_Full_description(edited_name)


@step('I edit SKU with "{}"')
def i_edit_SKU(context, edited_name):
    i = ProductListPage(context.driver)
    i.i_edit_SKU(edited_name)


@step("click on import button")
def click_on_import(context):
    see_columns = ProductListPage(context.driver)
    see_columns.click_on_import()


@step("click on choose file")
def click_on_choose_file(context):
    see_columns = ProductListPage(context.driver)
    see_columns.click_on_choose_file()


@step("I click on Published checkbox")
def i_click_publish_checkbox(context):
    publish_checkbox = ProductListPage(context.driver)
    publish_checkbox.i_click_publish_checkbox()
