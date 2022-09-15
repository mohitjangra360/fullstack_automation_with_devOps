from behave import *

from Pages.ProductListPage import ProductListPage


@step("I should see columns in Product list")
def i_should_see_columns(context):
    see_columns = ProductListPage(context.driver)
    see_columns.i_should_see_product_column()


@given("click on import button")
def click_on_import(context):
    see_columns = ProductListPage(context.driver)
    see_columns.click_on_import()


@step("click on choose file")
def click_on_choose_file(context):
    see_columns = ProductListPage(context.driver)
    see_columns.click_on_choose_file()
