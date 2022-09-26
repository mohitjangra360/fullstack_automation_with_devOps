from behave import *

from Pages.Catalog_Products_Page_Object import Catalog_Product


@step('I should see "Add new" button')
def i_see_add_new_btn(context):
    btn = Catalog_Product(context.driver)
    btn.i_see_add_new_btn()


@step("I click on add new button")
def click_on_add_new_cust_btn(context):
    btn = Catalog_Product(context.driver)
    btn.click_on_add_new_cust_btn()


@step('I should see "Download catalog as pdf" button')
def i_see_download_catalog_pdf_btn(context):
    btn = Catalog_Product(context.driver)
    btn.i_see_download_catalog_pdf_btn()


@step('I click on "Download catalog as pdf" button')
def i_click_on_download_catalog_btn(context):
    btn = Catalog_Product(context.driver)
    btn.i_click_on_download_catalog_btn()


@step('I should see "Export" button')
def i_see_export_btn(context):
    btn = Catalog_Product(context.driver)
    btn.i_see_export_btn()


@step("I click On Export button")
def i_click_on_export_btn(context):
    btn = Catalog_Product(context.driver)
    btn.i_click_on_export_btn()


@step("I should see Export to XML (all found)")
def i_see_export_to_xml_all(context):
    btn = Catalog_Product(context.driver)
    btn.i_see_export_to_xml_all()


@step("I should see Import button")
def i_see_import(context):
    btn = Catalog_Product(context.driver)
    btn.i_see_import()


@step("I click on import button")
def i_click_on_import(context):
    btn = Catalog_Product(context.driver)
    btn.i_click_on_import()


@step("I should see choose file popup box")
def i_see_choose_file_popup_box(context):
    btn = Catalog_Product(context.driver)
    btn.i_see_choose_file_popup_box()


@step("I should see Delete(Selected) button")
def i_see_delete_btn(context):
    btn = Catalog_Product(context.driver)
    btn.i_see_delete_btn()


@step("I click on delete(selected) button")
def i_click_on_delete_btn(context):
    btn = Catalog_Product(context.driver)
    btn.i_click_on_delete_btn()


@step("I should see Export to XML (selected)")
def i_see_export_to_xml_selected(context):
    btn = Catalog_Product(context.driver)
    btn.i_see_export_to_xml_selected()


@step("I should see Export to Excel (all found)")
def i_see_export_to_excel_all(context):
    btn = Catalog_Product(context.driver)
    btn.i_see_export_to_excel_all()


@step("I should see Export to Excel (selected)")
def i_see_export_to_excel_selected(context):
    btn = Catalog_Product(context.driver)
    btn.i_see_export_to_excel_selected()


@step('I should Enable checkbox of "{}"')
def set_mail_for_cust(context, mark):
    checkbox = Catalog_Product(context.driver)
    checkbox.user_mark_product_as_new(mark)


@step("I set Email")
def set_mail_for_cust(context):
    btn = Catalog_Product(context.driver)
    btn.set_mail_for_cust()


@step('I set Password "{}"')
def set_password(context, password):
    btn = Catalog_Product(context.driver)
    btn.set_password(password)


@step('I set First name as "{}"')
def set_firstname(context, firstname):
    btn = Catalog_Product(context.driver)
    btn.set_firstname(firstname)


@step('I set Last name as "{}"')
def set_lastname(context, lastname):
    btn = Catalog_Product(context.driver)
    btn.set_lastname(lastname)


@step('I select gender as "{}"')
def set_gender(context, gender):
    btn = Catalog_Product(context.driver)
    btn.set_gender(gender)


@step('I set dob as "{}"')
def set_dob(context, dob):
    btn = Catalog_Product(context.driver)
    btn.set_dob(dob)


@step('I set customer role as "{}"')
def set_customer_role(context, role):
    btn = Catalog_Product(context.driver)
    btn.set_customer_role(role)


@Step('I should able to see "{}" Button')
def user_should_able_to_see_Delete_Button(context, value):
    Delete_buttons = Catalog_Product(context.driver)
    Delete_buttons.user_should_able_to_see_Delete_Button(value)


@step('I should able to click "{}" Button')
def user_should_able_to_click_Delete_Button(context, value):
    click_delete = Catalog_Product(context.driver)
    click_delete.user_should_able_to_click_Delete_Button(value)


@step("I should able to click YES on Delete POPUP")
def user_should_able_to_click_YES_delete_popup(context):
    POPUP_delete = Catalog_Product(context.driver)
    POPUP_delete.user_should_able_to_click_YES_delete_popup()


@step("I should see Go directly to product SKU field")
def i_verify_product_sku_field(context):
    a = Catalog_Product(context.driver)
    a.i_verify_product_sku_field()


@step("I should able to enter product SKU {}")
def enter_product_SKU(context, sku):
    a = Catalog_Product(context.driver)
    a.enter_product_SKU(sku)


@step("I should able to click on Go button")
def i_click_on_go_btn(context):
    a = Catalog_Product(context.driver)
    a.i_click_on_go_btn()


@step("I should see SKU {} on edit page of that product")
def verify_edit_page_of_that_product(context, value):
    a = Catalog_Product(context.driver)
    a.verify_edit_page_of_that_product(value)


@step("I should see see product table")
def see_product_table(context):
    a = Catalog_Product(context.driver)
    a.i_should_see_product_table()


@step("I should see the product {} field")
def i_should_see_product_field(context, field_name):
    a = Catalog_Product(context.driver)
    a.i_should_see_product_field(field_name)


@step("I should see edit button of product {} & able to click on that")
def i_should_see_edit_btn_and_click(context, product):
    a = Catalog_Product(context.driver)
    a.i_should_see_edit_btn_and_click(product)


@step("I should able to change product {} field by {} with tag {} & save it")
def i_change_field_and_save(context, field, new_value, tag):
    a = Catalog_Product(context.driver)
    a.i_change_field_and_save(field, new_value, tag)


@step("I should able to change product cost field by {} & save it")
def i_change_cost_and_save(context, cost):
    a = Catalog_Product(context.driver)
    a.i_change_product_cost_and_save(cost)


@step("I should able to select product to delete")
def i_select_product_to_delete(context):
    select = Catalog_Product(context.driver)
    select.i_select_product_to_delete()


@step('I see search result by Warehouse and count number of items')
def step_impl(context):
    searchbtn = Catalog_Product(context.driver)
    searchbtn.i_see_search_result_by_warehouse()


@step('I should see data table')
def i_set_price(context):
    table = Catalog_Product(context.driver)
    table.i_should_see_table()


@step('I should click all items checkboxes')
def step_impl(context):
    click_checkboxes = Catalog_Product(context.driver)
    click_checkboxes.user_should_able_to_click_all_checkboxes()


@step('I should edit "{}" details by click "{}"')
def step_impl(context, productfullname, clickedit):
    edit = Catalog_Product(context.driver)
    edit.select_edit_by_productname(productfullname, clickedit)


@step('I select manufacturers "{}"')
def i_select_manufacturers(context, first):
    select = Catalog_Product(context.driver)
    select.select_categories_manufacturers(first)


@step('Click "{}"')
def i_set_price(context, select):
    s = Catalog_Product(context.driver)
    s.save_product_details(select)


@step("I should see saved successfully message")
def i_should_see_saved_successfully_message(context):
    s = Catalog_Product(context.driver)
    s.verify_success_save()


@step('I set product name "{}"')
def i_set_products_name(context, product_name):
    btn = Catalog_Product(context.driver)
    btn.i_set_products_name(product_name)


@step('I set short description "{}"')
def i_set_short_description(context, short_descp):
    btn = Catalog_Product(context.driver)
    btn.i_set_short_description(short_descp)


@step('I set full description "{}"')
def i_set_full_description(context, full_descp):
    btn = Catalog_Product(context.driver)
    btn.i_set_full_description(full_descp)


@step('I select categories first "{}" and second "{}"')
def i_select_categories(context, first, second):
    select = Catalog_Product(context.driver)
    select.select_categories(first, second)


@step('I set Product tags "{}"')
def i_set_product_tag(context, tag):
    producttags = Catalog_Product(context.driver)
    producttags.set_product_tags(tag)


@step('I set Product type "{}"')
def i_set_product_type(context, types):
    producttype = Catalog_Product(context.driver)
    producttype.set_product_type(types)


@step('I set Vendor type "{}"')
def i_set_Vendor_type(context, type):
    vendortype = Catalog_Product(context.driver)
    vendortype.set_vendor_type(type)


@step('I set Available start date "{}"')
def i_set_available_start_date(context, startdate):
    date = Catalog_Product(context.driver)
    date.set_available_start_date(startdate)


@step('I set Available end date "{}"')
def i_set_available_start_date(context, enddate):
    date = Catalog_Product(context.driver)
    date.set_available_end_date(enddate)


@step('I set price "{}"')
def i_set_price(context, price):
    pri = Catalog_Product(context.driver)
    pri.set_price(price)


@step('I set shipping weight "{}"')
def i_set_weight(context, weight):
    wei = Catalog_Product(context.driver)
    wei.set_shipping_weight(weight)


@step('I set Minimum qty "{}"')
def i_set_min_qty(context, qty):
    quantity = Catalog_Product(context.driver)
    quantity.set_Minimum_cart_qty(qty)


@step('I set Maximum qty "{}"')
def i_set_min_qty(context, qty):
    quantity = Catalog_Product(context.driver)
    quantity.set_Max_cart_qty(qty)
