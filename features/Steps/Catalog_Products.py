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
